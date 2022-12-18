# pybank

print("\nFinancial Analysis")
print("\n---------------------------------------------------------------------")

#Module
import os
import csv

#Lists to store the Date and Profit/Losses data
date = []
profit_losses = []
change_in_profit = []

#Set path for the file
csv_path = os.path.join("Resources","budget_data.csv")

previous_profit = 0
#open the file 
with open(csv_path) as csvfile:
    
    # Initialize csv.writer
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    
    # Read through each row of data after the header 
    for anyrow in csvreader:
        
        # append the date from the data to the data list
        date.append(anyrow[0])
        
        profit_losses.append(float(anyrow[1]))
        
        csv_header = next(csvreader)
        # convert the Profit/Losses data into a float and append it to the profit_losses list
        change_in_profit.append(float(anyrow[1]) - previous_profit)
        previous_profit = float(anyrow[1])


#calulate and print the total number months & print the result       
total_months = len(date)
print("\nTotal Months: " + str(total_months))

# calculate the total profit and losses & print the result
total = sum(profit_losses)
print("\nTotal: $"+str(total))


#the average change in profit is calculated by dividing the total change with the total number
#change_in_profit.remove(0)
total_change_in_profit = sum(change_in_profit)
#print(total_change_in_profit)
average = round(total_change_in_profit/(len(date)-1))

#print the average change in profit
print("\nAverage Change: $" + str(average))


# determine the maximum change in profit 
greatest_increase = max(change_in_profit)
# determine the index value of the maximum change in profit 
x = change_in_profit.index(greatest_increase)
# print the date & value of for the maximum change in profit 
print("\nGreatest Increase in Profits: " + date[x] + " ($" + str(greatest_increase) + ")")


# determine the biggest loss in profit  
greatest_decrease = min(change_in_profit)
# determine the index value of the biggest loss in profit
y = change_in_profit.index(greatest_decrease)
# print the date & value of for the biggest loss in profit
print("\nGreatest Decrease in Profits: " + date[y] + " ($" + str(greatest_decrease) + ")")

