import os 
import csv 

budget_csv = os.path.join("Resources", "budget_data.csv")


# read in the csv file
with open (budget_csv, 'r') as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
    # Format print
    print("Financial Analysis")
    print("----------------------------")

# Establish Variables
    header = next(csv_reader)
    total_months = 0
    total_net_amount = 0
    changed_per_month = []
    previous_month = 0
    allmonths = []

# Loop through to find totals 
    for row in csv_reader:
        
    # Calculate total months
        total_months = total_months + 1
    # Calculate total price amount
        total_net_amount = total_net_amount + int(row[1])
    # The average change in revenue between each month in the dataset 
        if row[0]!= 'Jan-2010':
            change = int(row[1]) - previous_month
            changed_per_month.append(change) 
            previous_month = int(row[1]) 
            allmonths.append(row[0])
        else: 
            previous_month = int(row[1]) 

# The date and value of greatest increase and decrease in revenue  
    max_change_value = max(changed_per_month)
    min_change_value = min(changed_per_month)
    max_change_month = changed_per_month.index(max(changed_per_month)) 
    min_change_month = changed_per_month.index(min(changed_per_month)) 

        
    
# Output values
    print(f"Total Months: {total_months}")
    print(f"Total Net Amount: ${total_net_amount}")
    print(f"Average Change: ${sum(changed_per_month)/len(changed_per_month)}")
    print(f"Greatest increase in change: ${allmonths[max_change_month]} ${max_change_value}")
    print(f"Greatest decrease in change: ${allmonths[min_change_month]} ${min_change_value}")

