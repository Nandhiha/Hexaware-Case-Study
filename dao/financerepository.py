import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from entity.user import User
from entity.expense import Expense
from util.db_conn_util import get_connection
from exception.myexceptions import UserNotFoundException, ExpenseNotFoundException

class IFinanceRepository:
    def create_user(self, user):
        pass

    def create_expense(self, expense):
        pass

    def delete_user(self, user_id):
        pass

    def delete_expense(self, expense_id):
        pass

    def get_all_expenses(self, user_id):
        pass

    def update_expense(self, user_id, expense):
        pass

    def get_all_users(self):
        pass 


class FinanceRepositoryImpl(IFinanceRepository):
    
    def create_user(self, user):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                (user.get_username(), user.get_password(), user.get_email())
            )
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False

    def create_expense(self, expense):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO expenses (user_id, amount, category_id, date, description) VALUES (?, ?, ?, ?, ?)",
                (expense.get_user_id(), expense.get_amount(), expense.get_category_id(), expense.get_date(), expense.get_description())
            )
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Error creating expense: {e}")
            return False

    def delete_user(self, user_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False

    def delete_expense(self, expense_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM expenses WHERE expense_id = ?", (expense_id,))
            row = cursor.fetchone()
            if row is None:
                raise ExpenseNotFoundException(f"Expense with ID {expense_id} not found")
            cursor.execute("DELETE FROM expenses WHERE expense_id = ?", (expense_id,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Error deleting expense: {e}")
            return False

    def get_all_expenses(self, user_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM expenses WHERE user_id = ?", (user_id,))
            rows = cursor.fetchall()
            expenses = []
            for row in rows:
                expense = Expense(row.expense_id, row.user_id, row.amount, row.category_id, row.date, row.description)
                expenses.append(expense)
            cursor.close()
            conn.close()
            return expenses
        except Exception as e:
            print(f"Error fetching expenses: {e}")
            return []

    def update_expense(self, user_id, expense):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE expenses SET amount = ?, category_id = ?, date = ?, description = ? WHERE expense_id = ? AND user_id = ?",
                (expense.get_amount(), expense.get_category_id(), expense.get_date(), expense.get_description(), expense.get_expense_id(), user_id)
            )
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Error updating expense: {e}")
            return False

    def get_all_users(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            users = []
            for row in rows:
                user = User(row.user_id, row.username, row.password, row.email)
                users.append(user)
            cursor.close()
            conn.close()
            return users
        except Exception as e:
            print(f"Error fetching users: {e}")
            return []
