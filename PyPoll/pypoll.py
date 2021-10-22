import os 
import csv

# Path to collect data from resources folder
election_data_csv = os.path.join("Resources", "election_data.csv")



# Read in the csv file 
with open(election_data_csv, 'r') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')

    print("Election Results")
    print("----------------")

# Declare variables 
    header = next(csv_reader)
    row_count= 0


    for row in csv_reader:
            row_count = row_count + 1      





print(f"Total Votes: {row_count}")
