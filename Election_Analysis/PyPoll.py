

#Retrieve Data
import csv
import os

##load file
file_to_load = os.path.join("Resources", "election_results.csv")
##save file
file_to_save = os.path.join("Analysis", "election_analysis.txt")
#read and analyze election results
##set accumulator to zero
total_votes = 0
#declare candidate list
candidate_options = []
#declare candidate votes dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
##open results
with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)
     ##skip header
     headers = next(file_reader) 
     ##Analyze
     for row in file_reader:
    ###get total votes
        total_votes +=1 
    ###get candidates and their votes
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1
    
#Total number of votes cast
print(total_votes)

#A complete list of candidates who received votes
print(candidate_options)
#Total number of votes each candidate received
print(candidate_votes)
#Percentage of votes each candidate won
for candidate_options in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percent = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: Received {vote_percent} of the vote.")
#The winner of the election based on popular vote
if (votes > winning_count) and (vote_percent > winning_percentage):
    winning_count = votes
    winning_percentage = vote_percent
    winning_candidate = candidate_name
print(f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n")
winning_candidate_summary = (
f"----------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count}\n"
f"Winning percentage:  {winning_percentage:.1f}%\n"
f"----------------------------\n")
print(winning_candidate_summary)