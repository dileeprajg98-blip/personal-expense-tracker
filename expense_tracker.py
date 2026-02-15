expenses = []

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/etc): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }

    expenses.append(expense)
    print("✅ Expense added successfully!\n")

def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return

    print("\n📋 Expense List:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | ₹{exp['amount']} | {exp['note']}")
    print()

def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Expense: ₹{total}\n")

while True:
    print("=== Personal Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("👋 Exiting... Bye!")
        break
    else:
        print("❌ Invalid choice. Try again.\n")
