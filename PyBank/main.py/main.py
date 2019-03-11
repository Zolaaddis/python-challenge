# Modules
import os
import csv
 
# Set path for file 
csvpath = os.path.join("budget_data.csv")
   
with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader) 
        
        profit_loss_list = list()
 
# Read each row using csvreader and append to list profit_loss_list[].
        for row in csvreader:
            profit_loss_list.append(row)
 
# Sum each months profit (loss) over entire period
total_profit_loss = 0
for row in profit_loss_list:
    total_profit_loss = total_profit_loss + int(row[1])
    
# Numer of months
length = len(profit_loss_list)
 
# Initialization of variables
sum_of_profit_loss_change = 0
greatest_increase_in_profit = 0
greatest_decrease_in_profit = 0
 
# Find month over month difference in profit (loss) amount over entire period.

for i in range(length-1):
    profit_loss_change = int(profit_loss_list[i+1][1]) - int(profit_loss_list[i][1])
 
    if profit_loss_change >= greatest_increase_in_profit:
        greatest_increase_in_profit = profit_loss_change
        greatest_increase_month = profit_loss_list[i+1][0]
 
    if profit_loss_change < greatest_decrease_in_profit:
        greatest_decrease_in_profit = profit_loss_change
        greatest_decrease_month = profit_loss_list[i+1][0]
 
    sum_of_profit_loss_change = sum_of_profit_loss_change + profit_loss_change
 
 
# caluclate the average chagne in profit (loss) over entire period         
average_change = sum_of_profit_loss_change/(length-1)
 
print('Financial Analysis')
print('-------------------------')
print(f'Total Months: {length}')
print(f'Total: ${total_profit_loss}')
print('Average Change: ${0:.2f}'.format(average_change))
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_in_profit})')
print(f'Greatest Decrease in Profits: {greatest_increase_month} (${greatest_decrease_in_profit})')
  
 
# Export a text file with the results
text_file = open("Financial_Analysis.txt", "w")
text_file.write('Financial Analysis'+'\n')
text_file.write('-------------------------'+'\n')
text_file.write(f'Total Months: {length}'+'\n')
text_file.write('Average Change: ${0:.2f}'.format(average_change)+'\n')
text_file.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_in_profit})'+'\n')
text_file.write(f'Greatest Decrease in Profits: {greatest_increase_month} (${greatest_decrease_in_profit})'+'\n')