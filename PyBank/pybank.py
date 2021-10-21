import os 
import csv 

budget_csv = os.path.join("Resources", "budget_data.csv")






# read in the csv file
with open (budget_csv, 'r') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
    # Title = input("Financial Analysis")
    print("Financial Analysis")
    print("----------------------------")

    header = next(csv_reader)
    total_months = 0
    total_net_amount = 0
    changed_per_month = []
    previous_month = 0
    for row in csv_reader:
        total_months = total_months + 1
        total_net_amount = total_net_amount + int(row[1]
        if row[0]!= 'Jan-2010':
            change = int(row[1]) - previous_month
            changed_per_month.append(change) 
            previous_month = int(row[1]) 
        else: 
            previous_month = int(row[1]) 

        
    

    print(f"Total Months: {total_months}")
    print(f"Total Net Amount: {total_net_amount}")
    print(f"Average: {changed_per_month.sum()/len(changed_per_month)}")

    #     print(row)






