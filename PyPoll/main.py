
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
    candidates_options = []
    candidate_votes = {}
    percentages_of_candidate = {}
    winner_total = 0
    winner = ""

# Loop through data with algorithmic calculations to produce results
    for row in csv_reader:
        # Calculating the total amount of votes
        total_vote_count = total_vote_count + 1
        # Assigning 
        candidate_name = row[2]
        if candidate_name not in candidates_options:
            candidate_votes[candidate_name] = 0
            candidates_options.append(candidate_name)
        
winner = candidate_votes(max(candidate_name))
for i in candidate_votes:
        vote_percentage = (float(candidate_votes[i])/float(total_vote_count)*100)
        percentages.append(vote_percentage)

    

file_to_save = os.path.join("Analysis", "analysis.txt")
output = (
    f"Election Results" + '\n'
    f"-------------------" + '\n'
    f"Total Votes: {total_vote_count}" + '\n'
    f"-------------------" + '\n'
    f"Winner:{winner}"
)



# print output to terminal
print(output)

# export file to analysis text file

with open(file_to_save, 'w') as analysis_txt: 
    analysis_txt.write(output)




