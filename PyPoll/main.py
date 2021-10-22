import os 
import csv

# Path to collect data from resources folder
election_data_csv = os.path.join("Resources", "election_data.csv")



# Read in the csv file 
with open(election_data_csv, 'r') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')



# Declare variables 
    header = next(csv_reader)
    total_vote_count= 0
# Candidate option and vote counters
    candidates_options = []
    candidate_votes = {}

# Winning Candidate and Winning Count Tracker
    winning_candidate = ""
    winning_count = 0
# 
    for row in csv_reader:
        total_vote_count = total_vote_count + 1
        candidate_name = row[2]
        
       


file_to_save = os.path.join("Analysis", "analysis.txt")
output = ( 
    "Election Results" + '\n'
    "-------------------" + '\n'
    f"Total Votes: {total_vote_count}" + '\n'
    "-------------------" + '\n'
    f"{candidate_name}" + '\n'
)

# print output to terminal
print(output)

# export file to analysis text file

with open(file_to_save, 'w') as analysis_txt: 
    analysis_txt.write(output)