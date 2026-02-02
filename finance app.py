expenses = []  # list of all expense dictionaries

print("Welcome to Adhwaryu finance app")
print("--------------------------------")
print("Ab Hoga Kharcha Control")
print("--------------------------------")

while True:
    print("\n----MENU----")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    # OPTION 1: Add Expense
    if choice == 1:
        date = input("Enter date (DD/MM/YYYY): ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("\nExpense added successfully")

    # OPTION 2: View All Expenses
    elif choice == 2:
        if len(expenses) == 0:
            print("\nNo expenses added yet")
        else:
            print("\n------ All Expenses ------")
            for exp in expenses:
                print(f"Date: {exp['date']}, Category: {exp['category']}, "
                      f"Description: {exp['description']}, Amount: {exp['amount']}")
            print("--------------------------")

    # OPTION 3: Total Expenses
    elif choice == 3:
        total_expenses = 0
        for exp in expenses:
            total_expenses += exp['amount']

        print(f"\nYour TOTAL EXPENSE is: {total_expenses}")

    # OPTION 4: Exit
    elif choice == 4:
        print("\nThank you for using Adhwaryu finance app")
        break

    # Invalid Choice
    else:
        print("\nInvalid choice. Please try again.")
