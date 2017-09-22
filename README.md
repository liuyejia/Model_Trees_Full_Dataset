# Model_Trees_Full_Dataset

## Provenance

+ on-line sources: hockey data crawled from [NHL](https://www.nhl.com/), [Eliteprospects](http://www.eliteprospects.com/) and [Draft Analyst](https://www.thedraftanalyst.com/)
+ local sources: Databases are stored in cs-oschulte-01.cs.sfu.ca
   + Complete Table. This is the file to which we apply model tree learning
     + github name: players_drafted_1998_2008_with_CSS_rank.csv
     + Database Table Name: join_skater_and_season_stats_10_years
   + NHL season stats. Used to compute 7-years career stats.
     + github name: NHL_season_stats_1997_2017_original.csv
     + Database Table Name: NHL_season_stats_1998_2016_original
   + Draft Stats.
     + github name: elite_prospects_skaters_stats_1998_2008_original.csv
     + database name: elite_prospects_skaters_stats_1998_2008_original
  
## Semantics

Field Name| Explanation|
----------|------------|
id        | nhl.com id for NHL players, otherwise Eliteprospects.com id|
Draft Age | Age in Draft Year|
