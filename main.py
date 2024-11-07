# Expense Tracker Application Starter Code

import csv
import os

CSV_FILE = 'expenses.csv'

# Initialize the CSV file with headers if it doesn't exist
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'date', 'description', 'amount'])

# Read expenses from the CSV file
def read_expenses():
    expenses = []
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(row)
    return expenses

# Write expenses to the CSV file
def write_expenses(expenses):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'date', 'description', 'amount'])
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

# Add a new expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    amount = input("Enter the amount: ")

    expenses = read_expenses()
    expense_id = len(expenses) + 1  # Incremental ID based on the number of entries

    new_expense = {
        'id': expense_id,
        'date': date,
        'description': description,
        'amount': amount
    }
    expenses.append(new_expense)
    write_expenses(expenses)
    print("Expense added successfully.")

# List all expenses
def list_expenses():
    expenses = read_expenses()
    if not expenses:
        print("No expenses recorded.")
        return

    print("ID | Date       | Description         | Amount")
    print("---------------------------------------------")
    for expense in expenses:
        print(f"{expense['id']} | {expense['date']} | {expense['description']} | {expense['amount']}")

# Delete an expense by ID
def delete_expense():
    expense_id = input("Enter the ID of the expense to delete: ")
    expenses = read_expenses()
    updated_expenses = [exp for exp in expenses if exp['id'] != expense_id]

    if len(updated_expenses) == len(expenses):
        print("No expense found with that ID.")
    else:
        write_expenses(updated_expenses)
        print("Expense deleted successfully.")

# Main program loop
def main():
    initialize_csv()
    print("Welcome to the Expense Tracker Application!")
    
    while True:
        print("\nOptions:")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Delete expense")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            list_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
