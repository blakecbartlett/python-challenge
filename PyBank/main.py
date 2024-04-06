import os
import csv
csvpath = os.path.join('Resources','budget_data.csv')

#Initialize the variables
total_months = 0
total = 0
previous_month = 0
monthly_change = []
months = []

#Open the csv file and read the dataset
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile , delimiter = ',')
    
    #Skip the header row on the csv
    csv_header = next(csvreader)

    #Read each row of data after header and calculate total profit or loss and then changes
    for row in csvreader:
       total_months = total_months + 1
       total = total + int(row[1])
       monthly_profit_loss_change = int(row[1]) - previous_month
       monthly_change.append(monthly_profit_loss_change)
       months.append(row[0])
       previous_month = int(row[1])

#Calculate the average change
average_profit_loss_change = sum(monthly_change[1:]) / (total_months - 1)

#Calculate the greatest increase and decrease in profits adn their dates
greatest_profit_increase = max(monthly_change)
increase_profit_date = months[monthly_change.index(greatest_profit_increase)]
greatest_profit_decrease = min(monthly_change)
decrease_profit_date = months[monthly_change.index(greatest_profit_decrease)]

#Print the report
print(f"Financial Analysis") 
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_profit_loss_change:.2f}")
print(f"Greatest Increase in Profits: {increase_profit_date} (${greatest_profit_increase})")
print(f"Greatest Decrease in Profits: {decrease_profit_date} (${greatest_profit_decrease})")

#Turn the output into a .txt file
with open('analysis/anaylsis.txt', 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total}\n")
    output_file.write(f"Average Change: ${average_profit_loss_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {increase_profit_date} (${greatest_profit_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {decrease_profit_date} (${greatest_profit_decrease})\n")

