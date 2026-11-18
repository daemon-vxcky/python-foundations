import csv
import sys
import math

def validate_csv(csv_file, headers):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file)
    csv_headers = reader.fieldnames
    if csv_headers == headers:
        return True
    elif csv_headers is None:
        print('File is empty!')
        return False
    else:
        print(f"Headers are invalid, please fix them, the header must look like this {headers}")
        sys.exit(1)

def get_record_count():
    n = -1
    while n<1:
        try:
            n = int(input('Enter the no of records you would like to enter in the expense tracker'))
        except ValueError:
            print("Number of records must be an integer greater than or equal to 1")
    return n

def get_expense_details():
    exp_desc = input('Enter Description of the Expense: ')
    exp_category = input('Enter Category of the Expense: ')
    exp_amount = -1.0
    while not (math.isfinite(exp_amount) and exp_amount>0):
        try:
            exp_amount = float(input('Enter the Expense Amount greater than zero: '))
        except ValueError:
            print("Try to input integer only values")
    return [exp_desc, exp_category, exp_amount]

file_name = "expense_tracker.csv"
headers = ["Expense Description", "Category", "Amount"]
has_headers = False
with open(file_name, mode='a+', newline='') as csv_file:

    has_headers = validate_csv(csv_file=csv_file, headers=headers)
    csv_writer = csv.writer(csv_file)
    if not has_headers:
        csv_writer.writerow(headers)
    n = get_record_count()
    
    expense_rows = []
    for i in range(1,n+1):
        expense = get_expense_details()
        expense_rows.append(expense)
    if expense_rows:
        csv_writer.writerows(expense_rows)