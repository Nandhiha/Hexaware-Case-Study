class UserNotFoundException(Exception):
    def __init__(self, message="User not found"):
        self.message = message
        super().__init__(self.message)

class ExpenseNotFoundException(Exception):
    def __init__(self, message="Expense not found"):
        self.message = message
        super().__init__(self.message)
