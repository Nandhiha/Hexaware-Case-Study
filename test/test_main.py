import sys
import os
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from dao.financerepository import FinanceRepositoryImpl
from entity.user import User
from entity.expense import Expense
from exception.myexceptions import UserNotFoundException, ExpenseNotFoundException

class TestFinanceApp(unittest.TestCase):
    def setUp(self):
        self.repo = FinanceRepositoryImpl()

    def test_create_user(self):
        
        user = User(user_id=101, username="test_user_" + str(random.randint(1, 1000)), email="test@example.com", password="pass123")
        result = self.repo.create_user(user)
        self.assertTrue(result)

    def test_add_expense(self):
        expense = Expense(expense_id=0, user_id=1, amount=200.0, category_id=1, date='2025-04-17', description='test expense')
        result = self.repo.create_expense(expense)
        self.assertTrue(result)

    def test_user_not_found_exception(self):
        with self.assertRaises(UserNotFoundException):
            self.repo.get_all_expenses(9999)

    def test_expense_not_found_exception(self):
        with self.assertRaises(ExpenseNotFoundException):
            self.repo.delete_expense(9999)

    def test_view_all_users(self):
        users = self.repo.get_all_users()  
        self.assertIsInstance(users, list)

if __name__ == "__main__":
    unittest.main()
