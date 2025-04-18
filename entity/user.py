class User:
    def __init__(self, user_id=None, username=None, password=None, email=None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
