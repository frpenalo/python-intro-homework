import os
import csv
from datetime import datetime


file_path = os.path.join("..", "data", "expenses.csv")


# Check if the file exists
if not os.path.exists(file_path):
    print("Error: expenses.csv not found.")
else:

    expenses = []

    # Read the CSV file
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)


    # Filter Food expenses
    food_expenses = []

    for expense in expenses:
        if expense["category"] == "Food":
            food_expenses.append(expense)


    # Calculate total
    total = 0

    for expense in food_expenses:
        total = total + expense["amount"]


    # Get today's date
    today = datetime.now().strftime("%B %d, %Y")


    # Write the report
    with open("food_report.txt", "w") as report:

        report.write(f"Food Expense Report — generated {today}\n")

        for expense in food_expenses:
            report.write(
                f'{expense["date"]}: ${expense["amount"]:.2f}\n'
            )

        report.write(f"Total: ${total:.2f}")


    print("food_report.txt created.")