import re
import requests
from bs4 import BeautifulSoup, Comment, Tag
import urllib.parse

from commit2db import MysqlConnection

YEAR_URL = 'https://www.basketball-reference.com/draft/NBA_{year}.html'
HEADERS = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2171.95 Safari/537.36'}


def regex_wrapper(found: list) -> str:
  return found[0] if found else ''


def get_player_info(soup: Tag) -> dict:
  meta_soup = soup.find(id='meta')
  player_data = {}
  player_data['name'] = meta_soup.h1.get_text()
  
  all_paragraph = meta_soup.select('div > p')
  
  meta_data = meta_soup.get_text().replace('\n', ' ')
  height, weight = regex_wrapper(re.findall(r'\((\d+)cm.*?(\d+)kg', meta_data))
  player_data['position'] = regex_wrapper(re.findall(r'Position\:?\s+(.*?)\s+▪', meta_data))
  player_data['shoots'] = regex_wrapper(re.findall(r'Shoots\:?\s+(\w+\s?\w+)', meta_data))
  player_data['height'] = int(height)
  player_data['weight'] = int(weight)
  
  if 'College' in meta_data:
    all_links = [x for x in meta_soup.find_all('a')]
    result = list(filter(lambda x: 'college' in x['href'], all_links))[0]
    player_data['college'] = result.get_text()
  
  try:
    player_data['born'] = meta_soup.find(id='necro-birth')['data-birth']
    player_data['team'] = regex_wrapper(re.findall(r'Team\:?\s+(\w+\s?\w+)', meta_data))
    player_data['nba_debut'] = all_paragraph[-2].a.get_text()
  except Exception:
    print("He doesn't have team or nba_debut...")
  return player_data


def str2float(string: str, default=None):
  try:
    return float(string)
  except ValueError:
    if default == None:
      return string
    else:
      return default


def get_career_data(soup: Tag) -> dict:
  try:
    career_data = soup.find('div', {'class': 'stats_pullout'})
    career_data = career_data.select('div > p')[2:]
    career_data = [str2float(x.get_text(), 0) for x in career_data]
    player_career = {}
    player_career['G'] = career_data[1]
    player_career['PTS'] = career_data[3]
    player_career['TRB'] = career_data[5]
    player_career['AST'] = career_data[7]
    player_career['FG'] = career_data[9]
    player_career['FG3'] = career_data[11]
    player_career['FT'] = career_data[13]
    player_career['eFG'] = career_data[15]
    player_career['PER'] = career_data[17]
    player_career['WS'] = career_data[19]
  except Exception:
    raise LookupError
  return player_career


def get_college_data(soup: Tag) -> dict:
  all_comments = soup.findAll(text=lambda x: isinstance(x, Comment))
  try:
    comment = list(filter(lambda x: 'College Table' in x, all_comments))[0]
  except IndexError:
    raise LookupError
  comment = BeautifulSoup(comment, 'html.parser')
  career_tr = comment.select('tfoot > tr')[0]
  
  def get_each_season(tr_soup: Tag):
    season_data = {}
    season_data['season'] = tr_soup.th.get_text()
    all_td = [str2float(x.get_text(), 0) for x in tr_soup.findAll('td')][-7:]
    all_columns = ['FG', '3P', 'FT', 'MP', 'PTS', 'TRB', 'AST']
    for index, column in enumerate(all_columns):
      season_data[column] = all_td[index]
    return season_data
  
  career_tr = get_each_season(career_tr)
  return career_tr


def get_person(url: str) -> tuple:
  html_page = requests.get(url, headers=HEADERS)
  html_page = html_page.content.decode('utf-8')
  drink_soup = BeautifulSoup(html_page, 'html.parser')
  player_info = get_player_info(drink_soup)
  try:
    career_data = get_career_data(drink_soup)
  except LookupError:
    career_data = {}
  try:
    college_data = get_college_data(drink_soup)
  except LookupError:
    college_data = {}
  return player_info, career_data, college_data


def get_person_list_by_year(year: int) -> list:
  url = YEAR_URL.format(year=year)
  year_html = requests.get(url, headers=HEADERS).content.decode('utf-8')
  year_soup = BeautifulSoup(year_html, 'html.parser')
  year_soup = year_soup.find(id='stats')
  player_list = year_soup.select('tbody > tr')
  
  def handle_one_player(player: Tag) -> tuple:
    try:
      pk = player.find('td', {'data-stat': 'pick_overall'}).get_text()
      url = player.find('td', {'data-stat': 'player'}).a['href']
    except:
      return ()
    return urllib.parse.urljoin(YEAR_URL, url), int(pk)
  
  player_list = [handle_one_player(x) for x in player_list]
  return player_list


def test(url: str):
  mysql = MysqlConnection()
  try:
    player_info, career_data, college_data = get_person(url)
  except IndexError:
    print("No college data")
    return
  player_info['draft_year'] = 9999
  player_info['ID'] = 999395
  print(player_info, career_data, college_data)
  mysql.save_to_db(player_info, career_data, college_data)

if __name__ == '__main__':
  mysql = MysqlConnection()
  for draft_year in range(2012, 2017):
    person_list = get_person_list_by_year(draft_year)
    person_list = filter(None, person_list)
    for person_url, pk in person_list:
      player_info, career_data, college_data = get_person(person_url)
      player_info['draft_year'] = draft_year
      player_info['pk'] = pk
      player_info['ID'] = draft_year * 100 + pk
      print(person_url)
      mysql.save_to_db(player_info, career_data, college_data)