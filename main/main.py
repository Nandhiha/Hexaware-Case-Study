from dao.financerepository import FinanceRepositoryImpl
from entity.user import User
from entity.expense import Expense
from exception.myexceptions import UserNotFoundException, ExpenseNotFoundException

def show_menu():
    print("\nFinance Management System")
    print("1. Add User")
    print("2. Add Expense")
    print("3. View All Users")
    print("4. View All Expenses for a User")
    print("5. Delete User")
    print("6. Delete Expense")
    print("7. Update Expense")
    print("8. Exit")

def add_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    email    = input("Enter email: ")
    user     = User(username=username, password=password, email=email)
    if repo.create_user(user):
        print(" User added successfully!")
    else:
        print("Error adding user.")

def add_expense():
    try:
        user_id     = int(input("Enter user ID for the expense: "))
        amount      = float(input("Enter expense amount: "))
        category_id = int(input("Enter category ID: "))
        date        = input("Enter date (YYYY-MM-DD): ")
        desc        = input("Enter description: ")
        exp = Expense(user_id=user_id, amount=amount, category_id=category_id, date=date, description=desc)
        if repo.create_expense(exp):
            print("Expense added successfully!")
        else:
            print(" Error adding expense.")
    except ValueError as e:
        print(f"Invalid input: {e}")

def view_users():
    users = repo.get_all_users()
    if users:
        print("\nAll Users:")
        for u in users:
            print(f"User ID: {u.get_user_id()}, Username: {u.get_username()}, Password: {u.get_password()}, Email: {u.get_email()}")
    else:
        print("No users found.")


def view_expenses():
    try:
        user_id  = int(input("Enter user ID to view expenses: "))
        expenses = repo.get_all_expenses(user_id)
        if expenses:
            print(f"\nExpenses for User ID {user_id}:")
            for e in expenses:
                print(f"Expense ID: {e.get_expense_id()}, Amount: {e.get_amount()}, "
                      f"Category ID: {e.get_category_id()}, Date: {e.get_date()}, Desc: {e.get_description()}")
        else:
            print("No expenses found for this user.")
    except ValueError as e:
        print(f" Invalid input: {e}")

def delete_user():
    try:
        user_id = int(input("Enter user ID to delete: "))
        if repo.delete_user(user_id):
            print("User deleted successfully!")
        else:
            print("Error deleting user.")
    except ValueError as e:
        print(f"Invalid input: {e}")

def delete_expense():
    try:
        expense_id = int(input("Enter expense ID to delete: "))
        if repo.delete_expense(expense_id):
            print("Expense deleted successfully!")
        else:
            print("Error deleting expense.")
    except ValueError as e:
        print(f" Invalid input: {e}")

def update_expense():
    try:
        user_id     = int(input("Enter user ID: "))  
        expense_id  = int(input("Enter expense ID to update: "))
        amount      = float(input("Enter new amount: "))
        category_id = int(input("Enter new category ID: "))
        date        = input("Enter new date (YYYY-MM-DD): ")
        desc        = input("Enter new description: ")

        exp = Expense(
            expense_id=expense_id,
            user_id=user_id,
            amount=amount,
            category_id=category_id,
            date=date,
            description=desc
        )

        if repo.update_expense(user_id, exp):  
            print("Expense updated successfully!")
        else:
            print(" Error updating expense. Make sure the expense ID and user ID are correct.")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    repo = FinanceRepositoryImpl()
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_user()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            view_users()
        elif choice == '4':
            view_expenses()
        elif choice == '5':
            delete_user()
        elif choice == '6':
            delete_expense()
        elif choice == '7':
            update_expense()
        elif choice == '8':
            print("Come again")
            break
        else:
            print("Invalid choice.")
