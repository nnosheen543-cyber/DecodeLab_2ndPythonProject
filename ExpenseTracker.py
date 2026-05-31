# Enhanced Expense Tracker

total = 0
count = 0
print("\n.........DecodeLab_Project2................")
print("===== Expense Tracker =====")
print(".........DecodeLab_Project2................\n")

while True:
    expense = input("Enter expense amount (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    try:
        expense = float(expense)

        if expense < 0:
            print("Expense cannot be negative!")
            continue

        total += expense
        count += 1

    except ValueError:
        print("Please enter a valid number!")

print("\n===== Expense Summary =====")
print("Total Expenses Entered:", count)
print("Total Amount Spent:", total)

if count > 0:
    print("Average Expense:", round(total / count, 2))