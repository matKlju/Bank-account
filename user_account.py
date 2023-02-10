"""

user account module

create user
read user - load user
update user - change, save user

"""
import pickle
from sys import exit as sys_exit
from pyinputplus import inputMenu, inputNum


class Account:
    """User account object"""

    def __init__(self, account_name, password, balance=0.0):
        self.account_name = account_name
        self.balance = balance
        self.password = password

    def display_account(self):
        """Show account and Balance"""

        print(f'\nAccount: {self.account_name}\nBalance: {self.balance} €')

    def display_balance(self):
        """Show only balance"""

        print(f'\nBalance: {self.balance} €')

    def withdraw(self):
        """Take money out"""

        while True:
            amount = inputNum('Amount: ', min=0)
            if amount > self.balance:
                print('Not enough resources!')
            else:
                self.balance -= amount
                break

    def deposit(self):
        """Put money in"""

        amount = inputNum('Amount: ', min=0)
        self.balance += amount


def save_account(user):
    """Save pickled file"""

    with open(f'{user.account_name}.dat', 'wb') as save_file:
        pickle.dump(user, save_file)


def _check_password(account):
    """Validate password"""

    tries = 3
    while tries > 0:
        user_password = input(f'Attempts x{tries}\nEnter password: ')
        if user_password == account.password:
            print('Correct')
            return True
        print('Incorrect password!')
        tries -= 1


def load_account():
    """Load pickled file"""

    while True:
        account_name = input('Account name: ')

        try:
            with open(f'{account_name}.dat', 'rb') as load_file:
                account = pickle.load(load_file)

            if _check_password(account):
                return account

            print('Access denied!\nTry again')
            break

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

    account_name = input('Name: ').lower()             # account name

    psw = _assign_password()                    # assign and verify password
    user_account = Account(account_name, psw)   # create user account object
    save_account(user_account)

    return user_account


def get_account():
    """Return account object"""

    choice = inputMenu(['New account', 'Old account', 'Quit'], numbered=True)

    if choice == 'New account':
        return new_account()         # create new account

    if choice == 'Old account':
        return load_account()        # load old account

    if choice == 'Quit':
        sys_exit()
