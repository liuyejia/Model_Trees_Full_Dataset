# Model_Trees_Full_Dataset

## Provenance

+ on-line sources: hockey data crawled from [NHL](https://www.nhl.com/), [Eliteprospects](http://www.eliteprospects.com/) and [Draft Analyst](https://www.thedraftanalyst.com/)
+ local sources: Databases are stored in cs-oschulte-01.cs.sfu.ca

Github Name                                 |Database Table Name                  | Meaning
-----------|--------------------|------|
players_drafted_1998_2008_with_CSS_rank.csv|join_skater_and_season_stats_10_years|This is the file to which we apply model tree learning|
NHL_season_stats_1997_2017_original.csv |NHL_season_stats_1998_2016_original | NHL season stats. Used to compute 7-years career stats |
elite_prospects_skaters_stats_1998_2008_original.csv | elite_prospects_skaters_stats_1998_2008_original| Used to compute draft stats|

