import os 
import csv 

budget_csv = os.path.join("Resources", "budget_data.csv")






# read in the csv file
with open (budget_csv, 'r') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
    Title = input("Financial Analysis")
    print("----------------------------")


