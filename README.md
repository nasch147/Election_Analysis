# Colorado Board of Elections: Audit and Analysis of Election Data
## Overview and Background
The Colorado Board of Elections has requested assistance with the tabulation, analysis, and audit of election data from one of its congressional districts. As part of this project, I was tasked with assisting Board of Election employees with determining several key pieces of information from raw aggregations of voter data provided to me in a comma separated file "csv". The csv file had three columns of data giving the ballot id, the county where the vote was cast, and the candidate selected on the ballot. From the raw data i was asked to tabulate the total votes cast in the election, the total votes for each candidate, and the total votes for each county. From these totals, we can calculate the percentages of the total vote that each county and candidate received in the election. This data will also tell us the eventual winner of the election.  Given that the preservation of the integrity of the raw data is essential to this project, the analysis was done using the python coding language which would allow us to read the data without needing to manipulate and alter the raw csv file.
## Audit Results
### The following bullets describe the outcomes of the election given by the data:
- Votes Cast: 369,711
- Votes Cast by County
  County        | Votes (% Total)
  ------------- | -------------
  Denver        | 306,055 (82.8%)
  Jefferson     | 38,855 (10.5%)
  Arapahoe      | 24,801 (6.7%)
  
  - As the most populous county in the precinct, Denver county had the most votes capturing well over three fourths of the total votes cast in the election. 

- Votes Cast by Candidate
  County        | Votes (% Total)
  ------------- | -------------
  Diana DeGette           | 272,892 (73.8%)
  Charles Casper Stockham | 85,213 (23.0%)
  Raymon Anthony Doane    | 11,606 (6.7%)
  
  - Ms. DeGette won the election receiving 272,892 votes or 73.8% of the total votes cast in the election. 

## Summary
The utility, ease-of-use, and agility of the python script generated for this project is evident in the results it has yielded for the board. With minimal modifications, the script could also be utilized for a variety of other purposes by the Board especially as it pertains to efficiently analyzing Colorado election data. One of the primary advantages is that the code does not need to be modified to accommodate files with differing categorical values, titles, or other naming conventions. 

![Load and Save Files](/Resources/load_save%20files.png)

The script allows for the reading of any csv file containing board election data. By simply altering the file path (orange script), the board is able to analyze any csv it wishes and save the results to a text file yielding an analysis of the data and preserving the csv files themselves. The script could also be scaled to allow for multiple csv's to be read and analyzed in a significantly expedited fashion as compared to manual analysis of each file individually. 

![Lists and Dictionaries](/Resources/Lists_Dictionaries.png)

The script also utilizes empty list and dictionary sets (key and value pairs) which are populated using the data within the csv itself obviating the need for altering the script significantly from project to project. Variable names in the script are largely arbitrary and can be replaced as needed for the specific task. 

![Candidate Outcomes](/Resources/Candidate_Outcomes.png)
![County Outcomes](/Resources/County_Outcomes.png)

The script also provides analysis output at both the geographic and candidate level which are key aspects an any election, not just the subject election described herein.

----------------
# Precinct Data - [CO Election_Data](/Resources/election_results.csv)
 
