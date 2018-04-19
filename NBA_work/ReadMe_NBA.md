### Drafting NBA Players Based on Their College Performance

+ Data is crawled from https://www.basketball-reference.com/draft/NBA_[1985-2011].html
+ Python scripts can be found here: https://github.com/HaoPatrick/NBA_draft_crawler
+ Predictors: NCAA college stats

Field | Explanation|
--------- | ----------- |
age | * |
height | * |
weight | * |
position| * |
shoots | shoots made in the draft year |
draft_g | games played in the draft year|
mp | Minutes Played in the draft year|
draft_fg | Field Goals in the draft year|
fga | Field Goal Attempts in the draft year|
3p | 3-Point Field Goals in the draft year|
3pa | 3-Point Field Goals Attempt in the draft year|
draft_ft | Free Throws in the draft year|
fta |Free Throws Attempt in the draft year|
orb | Offensive Rebouds in the draft year|
draft_trb | Total Rebounds in the draft year|
draft_ast | Assits in the draft year|
draft_stl | Steals in the draft year|
draft_blk | Blocks in the draft year|
draft_tov | Turnovers in the draft year|
draft_pf | Personal Fouls in the draft year|
draft_pts | Points in the draft year|
mp_per | Minutes Played per game in the draft year|
pts_per |Points per game in college|
trb_per | Total Rebounds per game in college|
asb_per | Assist per game in college|
amature_honor | NCAA all_American(1, 0)|
raw_data | If the player college stats exists, the value is 1, otherwise, is 0 |

+ Evaluation Metrics: Overall Pick(pk)

+ Response Variables: NBA stats

Field | Explanation|
--------- | ----------- |
career_g | games played in player's NBA career|
Career PER | A measure for player's per-minute performance, while adjusting for pace. A league-average PER is always 15.00, which permits comparisons of player performance across seasons.|
WinShare(WS) |  an estimate of the number of wins contributed by a player|
Career_WS/48 | an estimate of the number of wins contributed by a player per 48 minutes |


+ Reference Paper: https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/NBA_work/The%20Success%20of%20NBA%20Draft%20Picks-%20Can%20College%20Careers%20Predict%20NBA%20W.pdf

+ If a player's college stats are missing but having career stats, his college stats is replaced by the mean value of his draft year; If his career stats are missing, then his career stats are replaced by min(x)-std(x) of his draft year, since we think he is not good enough to play or have record in NBA. For the players missing both stats, we exclude them. Datasets can be found [here](https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/NBA_work/joined_drafted_all_players_original.csv) 

+ [Normalized datasets](https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/NBA_work/NBA_all_datasets_norm.csv)

+ The tree produced by Weka M5P:
The stats of playes drafted ***from 1985 to 2005*** are used as training datasets while the stats of players drafted ***from 2006 to 2011*** are testing datasets.

![NBA M5P tree](https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/NBA_work/M5P_Tree.png)

<sub>Position_Union_1 = (Small Forward,Point Guard and Shooting Guard and Small Forward,Power Forward and Shooting Guard and Small Forward,Power Forward,Small Forward and Point Guard and Shooting Guard,Small Forward and Power Forward,Point Guard,Shooting Guard and Small Forward and Point Guard,Point Guard and Shooting Guard,Small Forward and Shooting Guard,Small Forward and Shooting Guard and Power Forward,Small Forward and Power Forward and Center,Shooting Guard and Power Forward,Power Forward and Small Forward,Shooting Guard and Point Guard,Shooting Guard and Small Forward,Shooting Guard and Small Forward and Power Forward,Center and Power Forward,Power Forward and Center,Point Guard and Small Forward and Shooting Guard,Small Forward and Power Forward and Shooting Guard,Small Forward and Shooting Guard and Point Guard,Center and Small Forward and Power Forward,Power Forward and Center and Small Forward,Small Forward and Center and Power Forward,Center and Power Forward and Small Forward,Shooting Guard and Power Forward and Small Forward)</sub>

<sub>Position_Union_2 = (Center/Forward,Center and Small Forward,Small Forward and Center,Center,Shooting Guard and Point Guard and Small Forward,Power Forward and Small Forward and Shooting Guard,Shooting Guard,Small Forward,Point Guard and Shooting Guard and Small Forward,Power Forward and Shooting Guard and Small Forward,Power Forward,Small Forward and Point Guard and Shooting Guard,Small Forward and Power Forward,Point Guard,Shooting Guard and Small Forward and Point Guard,Point Guard and Shooting Guard,Small Forward and Shooting Guard,Small Forward and Shooting Guard and Power Forward,Small Forward and Power Forward and Center,Shooting Guard and Power Forward,Power Forward and Small Forward,Shooting Guard and Point Guard,Shooting Guard and Small Forward,Shooting Guard and Small Forward and Power Forward,Center and Power Forward,Power Forward and Center,Point Guard and Small Forward and Shooting Guard,Small Forward and Power Forward and Shooting Guard,Small Forward and Shooting Guard and Point Guard,Center and Small Forward and Power Forward,Power Forward and Center and Small Forward,Small Forward and Center and Power Forward,Center and Power Forward and Small Forward,Shooting Guard and Power Forward and Small Forward)</sub>

+ The results of leadnode and predicted_per_results, added to normalized datasets, can be found [here](https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/NBA_work/NBA_all_players_leafnode_results.csv), corresponding code is stored [here](https://github.com/sfu-cl-lab/Yeti-Thesis-Project/blob/master/NBA_work/code.py)

+ Results:
The Root Mean Squred Error of training datasets is ***5.31***, while ***6.16*** in testing datasets. The Pearson and Spearman correlation is summarized as following:

Datasets| Comparing Field | Pearson Correlation | Spearman Ranking Correlation |
--------| ------------- | ------------------- | -------------------- |
Training Datasets [1985-2005] | Overall Pick vs. Career Per | 0.23 | 0.42 |
Training Datasets [1985-2005]| M5P vs. Career Per | ***0.62*** | ***0.48*** |
Testing Datasets [2006-2011] | Overall Pick vs. Career Per | 0.42  | 0.39 |
Testing Datasets [2006-2011] | M5P vs. Career Per | ***0.55*** | ***0.43*** |





















