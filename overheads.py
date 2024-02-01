#OVERHEADS
fp2=Path.cwd()/"Overheads.csv"
overh=[]
expense_list = []
with fp2.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header


    # append overheads into the overh list
    for row in reader:
        #get the category and overheads for each record
        #and append to the overh list
        overh.append([row[0],float(row[1])])
# Opening the file in 'w' mode to write the summary report
file=open('summary_report.txt','w')
# Iterating over each record in the 'overh' list
for o in overh:
        # Extracting the expense value and appending it to the 'expense_list'
        expense = o[1]
        expense_list.append(expense)

    # Sorting the 'expense_list' to find the highest expense
expense_list.sort()
highest_expense = expense_list[-1]

    # Creating a list of dictionaries to store overhead names and their corresponding expenses
expense_dict_list = []
for o in overh:
        expense_dict = {
            "name": o[0],
            "overhead": o[1]
        }
        expense_dict_list.append(expense_dict)

    # Finding the overhead with the highest expense
for x in expense_dict_list:
        if x.get("overhead") == highest_expense:
            highest_overhead = x.get("name")
print(f'[HIGHEST OVERHEAD] {highest_overhead}:{highest_expense}')
    # Writing the result to the summary report file
file.write(f'[HIGHEST OVERHEAD] {highest_overhead}:{highest_expense}\n')
