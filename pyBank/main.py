# pybank

print("\nFinancial Analysis")
print("\n---------------------------------------------------------------------")

#Module
import os
import csv

#Lists to store the Date and Profit/Losses data
date = []
profit_losses = []

#Set path for the file
csv_path = os.path.join("Resources","budget_data.csv")

#open the file 
with open(csv_path) as csvfile:
    
    # Initialize csv.writer
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # append the content of each row in the date and Ppofit_losses list 
    for anyrow in csvreader:
        date.append(anyrow[0])
        profit_losses.append(anyrow[1])

#calulate and print the total number months        
print("\nTotal Months: " + str(len(date)))

# add the profit and losses
total = sum(profit_losses)
print("\nTotal: $"+str(total))

#
average = round(total/len(profit_losses),2)
print("\nAverage Change: $" + average)

#
greatest_increase = max(profit_losses)
x = profit_losses.index(greatest_increase)
print("\nGreatest Increase in Profits: " + date[x] + "($" + greatest_increase + ")")

#   
greatest_decrease = min(profit_losses)
y = profit_losses.index(greatest_decrease)
print("\nGreatest Decrease in Profits: " + date[y] + "($" + greatest_decrease + ")")

