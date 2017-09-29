# Model_Trees_Full_Dataset

## Provenance

+ on-line sources: hockey data crawled from [NHL](https://www.nhl.com/), [Eliteprospects](http://www.eliteprospects.com/) and [Draft Analyst](https://www.thedraftanalyst.com/). Thank you to David Wilson for letting us use his draft data set!
+ local sources: Databases are stored in cs-oschulte-01.cs.sfu.ca
   + NHL season stats. Used to compute 7-years career stats.
     + github name: NHL_season_stats_1997_2017_original.csv
     + Database Table Name: chao_draft.NHL_season_stats_1998_2016_original
   + Draft Stats.
     + github name: elite_prospects_skaters_stats_1998_2008_original.csv
     + database name: chao_draft.elite_prospects_skaters_stats_1998_2008_original
   + Complete Table. Combines NHL season stats and Draft Stats. This is the file on which we base our learning method.(po_PlusMinus were dropped due to missing values) 
     + github name: raw_datasets.csv
     + Database Table Name: chao_draft.join_skater_and_season_stats_10_years_without_po_plusminus
   + Processed Stats. Applying preprocessing steps to the complete raw data table.
     + Processing Steps: 
        1. sum_7yr_GP > 0 is entered in column gp_7_yr > 0 as target class label.
        2. null values for counts are converted to 0 (e.g. po_GP = null becomes po_GP = 0).
        3. countries -> country_group = USA, CAN, EURO. So European countries are lumped together (no disrespect intended).
        4. null values for CSS_rank are converted to the (maximum_rank + 1) of the corresponding year.
     + github name: preprocessed_datasets.csv
     + database name: chao_draft.join_skaters_preprocessed_without_po_PlusMinus
   + Normalized Stats. This is the input for model tree learning.
     + Processing Steps:
        1. standardize data to the same range, i.e. x := x - min(x)/(max(x) - min(x)), see [here](https://en.wikipedia.org/wiki/Feature_scaling). The max is chosen with respect to each cohort (cohort 1 has draft year 1998-2002, cohort 2 has draft year 2004-2008).
     + github name: normalized_datasets.csv
     + database name: chao_draft.norm_data_without_po_PlusMinus
  
## Semantics

Field Name| Explanation|
----------|------------|
id        | nhl.com id for NHL players, otherwise Eliteprospects.com id|
Draft Age | Age in Draft Year|
Country_group   | Nationality. Canada -> 'CAN', USA -> 'USA', countries in Europe -> 'EURO'|
Position  | Position in Draft Year. Left Wing -> 'L', Right Wing -> 'R', Center -> 'C', Defencemen -> 'D'| 
Overall   | Overall pick in NHL Entry Draft|
CSS_rank  | Central scouting service ranking in the draft year|
rs_GP     | Games played in regular seasons in the draft year|
rs_G      | Goals in regular seasons in the draft year|
rs_A      | Assists in regular seasons in the draft year|
rs_P      | Points in regular seasons in the draft year|
rs_PIM    | Penality_in_Minutes in regular seasons in the draft year|
rs_PlusMinus| Goal Differential in regular seasons in the draft year|
po_GP     | Games played in playoffs in the draft year|
po_G      | Goals in playoffs in the draft year|
po_A      | Assists in playoffs in the draft year|
po_P      | Points in playoffs in the draft year|
po_PIM    | Penality_in_Minutes in playoffs in the draft year|
po_PlusMinus|  Goal Differential in playoffs in the draft year|
sum_7yr_GP| Total games played in player's first 7 years of NHL career|
sum_7yr_TOI| Total Time_on_Ice in player's first 7 years of NHL career|
GP_7yr_greater_than_0| Played a game or not in player's first 7 years of NHL career|

