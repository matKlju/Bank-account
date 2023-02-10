"""

user account module

create user
read user - load user
update user - change, save user
delete user

"""
import pickle


class Account:
    """User account object"""

    def __init__(self, account_name, password, balance=0.0):
        self.account_name = account_name
        self.balance = balance
        self.password = password

    def display_account(self):
        print(f'Account: {self.account_name}\nBalance: {self.balance}')

    def display_balance(self):
        print(f'Balance: {self.balance}')

    def withdraw(self):
        amount = float(input('Amount: '))
        self.balance -= amount

    def deposit(self):
        amount = float(input('Amount: '))
        self.balance += amount


def save_account(user):
    """Save pickled file"""

    with open(f'{user.account_name}.dat', 'wb') as save_file:
        pickle.dump(user, save_file)


def load_account():
    """Load pickled file"""
    while True:
        account_name = input('Account name: ')
        if account_name == 'Q':
            break
        try:
            with open(f'{account_name}.dat', 'rb') as load_file:
                account = pickle.load(load_file)
            return account

        except FileNotFoundError:
            print('File not found')


def _assign_password():
    """Assign, verify, return"""

    while True:
        new_pwd = input('Password: ')
        check_pwd = input('Repeat password: ')
        if check_pwd == new_pwd:
            return new_pwd


def new_account():
    """Create new account"""

    account_name = input('Name: ')              # account name
    psw = _assign_password()                     # assign and verify password
    user_account = Account(account_name, psw)   # create user account object
    save_account(user_account)
    return user_account
