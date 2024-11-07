# expense-tracker-challenge
Coding Challenge: 
Expense Tracker Command-Line Application

# Challenge Description
Overview: The application should allow users to add, view, and delete expenses. Each expense entry should include a date, description, and amount.

# Requirements:
The application should:
Add a new expense (date, description, amount).
List all expenses.
Delete an expense by ID.
Data should be stored in a file (expenses.csv), so information persists between program runs.

# Detailed Instructions:
Add Expense: Prompt the user to enter the date, description, and amount. Save this entry to expenses.csv.
List Expenses: Display all expenses from the file, including each expense’s date, description, amount, and an ID for reference.
Delete Expense: Allow the user to delete an expense by entering the expense ID. Update the expenses.csv file accordingly.

# Data File Structure:
expenses.csv should have the following structure:
id,date,description,amount
1,2024-11-01,"Groceries",20.50
2,2024-11-02,"Transport",15.00

Each row represents an expense with a unique ID, date, description, and amount.

# Example Commands:

Add expense: add
List expenses: list
Delete expense: delete
Evaluation Criteria
Code Quality: Clean, readable, and organized code.
Data Handling: Proper handling of file reading and writing.
Functionality: Correct implementation of add, list, and delete features.
Error Handling: Handle invalid inputs and file-related errors.

## Submission Instructions
1. **Fork this repository** to your GitHub account.
2. **Clone your forked repository** to your local machine.
3. Complete the challenge and push your changes to your forked repository.
4. Submit your solution by creating a **pull request** to this repository.

