# To-Do-List
print("---Welcome to Expense Tracker---")
print("1. Add your Expense")
print("2. Delete Expense")
print("3. View Expense")
print("4. Add your Total Expense")
print("5. Clear All Expenses")
print("6. Exit")

while True:
    print("1. Add your Expense")
    print("2. Delete Expense")
    print("3. View Expense")
    print("4. Add your Total Expense")
    print("5. Clear All Expenses")
    print("6. Exit")

    user_choice = int(input("Enter the Option number: "))
    if user_choice == 1:
        expense_name = input(("Enter your expense name: "))
        expense_price = str(input("Enter your expense price: "))
        expense_set = [expense_name , expense_price]
        with open("Expense_tracker.txt" , "a") as file:
            file.writelines(expense_set)
    if user_choice == 6:
        print("Your expenses are tracked and saved!!\nHave a Nice day!! ")
        break
    if user_choice == 5:
        with open("Expense_tracker.txt" , "w") as file:
            file.write("")
            print("Your data is Cleared")