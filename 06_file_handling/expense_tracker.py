import csv

file_name = "expense_tracker.csv"
headers = ["Expense Description", "Category", "Amount"]
has_headers = False
with open(file_name, mode='a+', newline='') as csv_file:

    csv_file.seek(0)
    reader = csv.DictReader(csv_file)
    csv_headers = reader.fieldnames
    if csv_headers == headers:
        has_headers = True
    elif csv_headers is None:
        print('File is empty!')
        has_headers = False
    else:
        print(f"Headers are invalid, please fix them, the header must look like this {headers}")
        exit(0)

with open(file_name, mode='a+', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    if not has_headers:
        csv_writer.writerow(headers)
    n = int(input('Enter the no of records you would like to enter in the expense tracker'))
    expense_rows = []
    for i in range(1,n+1):
        exp_desc = input('Enter Description of the Expense: ')
        exp_category = input('Enter Category of the Expense: ')
        exp_amount = int(input('Enter the Expense Amount: '))
        while exp_amount<0:
            print("INVALID EXPENSE AMOUNT, ENTER ONLY POSITIVE VALUES")
            exp_amount = int(input('Enter the Expense Amount: '))

        expense_rows.append([exp_desc,exp_category,exp_amount])
    if expense_rows:
        csv_writer.writerows(expense_rows)