import os
import csv

# Path to the CSV file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#Initialiseing variables 
months = []
profit_losses = []
changes = []

# READ CSV file
with open(budget_data_csv, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_header = next(csv_reader) 
        
        # Start reading from the first data row
        first_row = next(csv_reader)
        months.append(first_row[0])
        previous_profit_loss = int(first_row[1])
        profit_losses.append(previous_profit_loss)

        for row in csv_reader:
                months.append(row[0])
                current_profit_loss = int(row[1])
                profit_losses.append(current_profit_loss)

                #Calculation of the Change
                changes.append(current_profit_loss - previous_profit_loss)
                previous_profit_loss = current_profit_loss

# Calculate required metrics
total_months = len(months)
total_profit_losses = sum(profit_losses)
average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_month = months[changes.index(greatest_increase) + 1]
greatest_decrease_month = months[changes.index(greatest_decrease) + 1]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Export the results to a text file
output_path = os.path.join('analysis', 'financial_analysis.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_losses}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
    








