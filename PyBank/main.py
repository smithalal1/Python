# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# Dependencies
import csv

# Files to analyze
file_to_analyze = "C:/Users/smith/Google Drive/UOR Homework/python-challenge/PyBank/budget_data.csv"
file_to_output = "C:/Users/smith/Google Drive/UOR Homework/python-challenge/PyBank/budget_analysis.txt"

# Variables to Track
total_months = 0
total_profit_loss = 0 
prev_profit_loss = 0
profit_loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
profit_loss_changes_list = []
month_of_change = []


# Read Files
with open(file_to_analyze) as profit_loss_data:
    reader = csv.DictReader(profit_loss_data)

    # Loop through all the rows of data we collect
    for row in reader:

        # Calculate the totals
        total_months = total_months + 1
        total_profit_loss = total_profit_loss + int(row["Profit/Losses"])
        # print(row)

        # Keep track of changes
        # profit_loss_change = int(row["Profit/Losses"]) - prev_profit_loss
        #Calculate the average change in revenue between months over the entire period
        profit_loss_change = float(row["Profit/Losses"])- prev_profit_loss
        if total_months > 1:
           profit_loss_changes_list = profit_loss_changes_list + [profit_loss_change]
        prev_profit_loss = float(row["Profit/Losses"])
        
        month_of_change = [month_of_change] + [row["Date"]]
        # print(profit_loss_change)

        # Reset the value of prev_profit_loss to the row I completed my analysis
        prev_profit_loss = int(row["Profit/Losses"])
        # print(prev_profit_loss)

        # Determine the greatest increase
        if (profit_loss_change > greatest_increase[1]):
            greatest_increase[1] = profit_loss_change
            greatest_increase[0] = row["Date"]

        if (profit_loss_change < greatest_decrease[1]):
            greatest_decrease[1] = profit_loss_change
            greatest_decrease[0] = row["Date"]

        # Add to the profit_loss_changes list
        #profit_loss_changes_list.append(int(row["Profit/Losses"]))

    # Set the profit-loss average
    profit_loss_avg = round((sum(profit_loss_changes_list) / len(profit_loss_changes_list)),2)

    
    # Show Output
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Profit/Losses: " + "$" + str(total_profit_loss))
    print("Average Change: " + "$" + str(round(sum(profit_loss_changes_list) / len(profit_loss_changes_list),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")   

# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Profit/Losses: " + "$" + str(total_profit_loss))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(profit_loss_changes_list) / len(profit_loss_changes_list),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")

