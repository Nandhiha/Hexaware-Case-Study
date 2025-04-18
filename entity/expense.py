class Expense:
    def __init__(self, expense_id=None, user_id=None, amount=None, category_id=None, date=None, description=None):
        self.expense_id = expense_id
        self.user_id = user_id
        self.amount = amount
        self.category_id = category_id
        self.date = date
        self.description = description

    def get_expense_id(self):
        return self.expense_id

    def set_expense_id(self, expense_id):
        self.expense_id = expense_id

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_category_id(self):
        return self.category_id

    def set_category_id(self, category_id):
        self.category_id = category_id

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description
