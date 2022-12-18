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


#open the file 
with open(csv_path) as csvfile:
    
    # Initialize csv.writer
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    
    # Read the second row next
    csv_first_row = next(csvreader)
   
    # append the date of the 2nd row
    date.append(csv_first_row[0])
    
    # append the Profit/Losses data of the 2nd row
    profit_losses.append(float(csv_first_row[1]))
    
    # initial profit/loss
    previous_profit = profit_losses[0]
    
    # Read through each row of data after the header 
    for anyrow in csvreader:
        
        # append the date data to list
        date.append(anyrow[0])
        
        # append the Profit/Losses data list
        profit_losses.append(float(anyrow[1]))
        
        # convert the Profit/Losses data into a float and append it to the profit_losses list
        change_in_profit.append(float(anyrow[1]) - previous_profit)
        previous_profit = float(anyrow[1])


#calulate and print the total number months & print the result       
total_months = len(date)
print("\nTotal Months: " + str(total_months))

# calculate the total profit and losses & print the result
total = round(sum(profit_losses))
print("\nTotal: $"+str(total))


#the average change in profit is calculated by dividing the total change with the total number
total_change_in_profit = sum(change_in_profit)
average = round(total_change_in_profit/(len(change_in_profit)),2)

#print the average change in profit
print("\nAverage Change: $" + str(average))


# determine the maximum change in profit 
greatest_increase = round(max(change_in_profit))
# determine the index value of the maximum change in profit 
x = change_in_profit.index(greatest_increase)
# print the date & value of for the maximum change in profit 
print("\nGreatest Increase in Profits: " + date[x+1] + " ($" + str(greatest_increase) + ")")


# determine the biggest loss in profit  
greatest_decrease = round(min(change_in_profit))
# determine the index value of the biggest loss in profit
y = change_in_profit.index(greatest_decrease)
# print the date & value of for the biggest loss in profit
print("\nGreatest Decrease in Profits: " + date[y+1] + " ($" + str(greatest_decrease) + ")")

