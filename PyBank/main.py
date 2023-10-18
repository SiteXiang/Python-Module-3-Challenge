import os
import csv

# Set the CSV file path
csv_path = "C:\\Users\\Sy X\\DATA CLASS\\EXCEL-HW\\Python-Module-3-Challenge\\PyBank\\Resources\\budget_data.csv"

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

# Read the CSV file
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        # Calculate the total number of months
        total_months += 1

        # Calculate the net total amount
        net_total += int(row[1])

        # Calculate Profit/Losses change and store it in a list
        if total_months > 1:
            profit_loss_change = int(row[1]) - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            months.append(row[0])

        previous_profit_loss = int(row[1])

# Calculate the average change
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Find the greatest increase and greatest decrease in profits along with their corresponding months
greatest_increase = max(profit_loss_changes)
greatest_increase_month = months[profit_loss_changes.index(greatest_increase)]
greatest_decrease = min(profit_loss_changes)
greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease)]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Export the results to a text file
output_path = "C:/Users/Sy X/DATA CLASS/EXCEL-HW/Python-Module-3-Challenge/PyBank/analysis/financial_analysis.txt"
with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
