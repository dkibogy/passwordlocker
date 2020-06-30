import random
class User:
    """
    class that generates new instances of users
    """
    user_list = []

    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def save_user(self):

        User.user_list.append(self)
    
    def delete_user(self):

        User.user_list.remove(self)
class Credentials:

    user_credentials = []

    def __init__(self, account_type, username, password):

        self.account_type = account_type
        self.username = username
        self.password = password
    def save_account(self):

        Credentials.user_credentials.append(self)
    
    def delete_account(self):

        Credentials.user_credentials.remove(self)

    @classmethod
    def show_accounts(cls):
        """
        method that will show all the accounts saved in our locker

        """
        return cls.user_credentials

    @classmethod
    def generate_password(cls):
        """
        method to generate passwords for our accounts
        """


