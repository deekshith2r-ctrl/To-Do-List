# To-Do-List
print("---Welcome to Expense Tracker---")
print("1. Add your Expense")
print("2. Delete Expense")
print("3. View Expense")
print("4. Add your Total Expense")
print("5. Clear All Expenses")
print("6. Exit")
i = 0

while True:
    print("1. Add your Expense")
    print("2. Delete Expense")
    print("3. View Expense")
    print("4. Add your Total Expense")
    print("5. Clear All Expenses")
    print("6. Exit")

    # 1 , 3 , 5 , 6 

    user_choice = int(input("Enter the Option number: "))
    if user_choice == 1:
        i = i+1
        expense_name = input(("Enter your expense name: "))
        expense_price = str(input("Enter your expense price: "))
        expense_set = [expense_name , expense_price]
        with open("Expense_tracker.txt" , "a") as file:
            file.write(f"{i}. Expense_name : {expense_name} , Expense_price: {expense_price} \n")
    if user_choice == 6:
        print("Your expenses are tracked and saved!!\nHave a Nice day!! ")
        break
    if user_choice == 5:
        with open("Expense_tracker.txt" , "w") as file:
            file.write("")
            print("Your data is Cleared")
    if user_choice == 3:
        with open("Expense_tracker.txt" , "r") as file:
            data = file.read()
            print(data)
    if user_choice == 2:
        with open("Expense_tracker.txt" , "r") as file:
            for line , line_num in enumerate(file):
                print(line+1)
                # print(line_num)
                splitted_lines = line_num.split()
                print(splitted_lines)
                delete_choice = int(input("Enter the serial number to be deleted: "))
                


    