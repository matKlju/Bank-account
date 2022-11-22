from data import *
from password import *


class User:

    def __init__(self, name, psw, balance):
        self.name = name
        self.psw = psw
        self.balance = balance


def old_account():
    while True:
        name = input('\nq to quit!\nAccount:\n>_')
        if name == 'q':
            break

        # read from data module return User object
        account = read_data(name)

        return account


def new_account():
    name = input('Name:\n>_')
    balance = '0'
    psw = new_password()

    account = User(name, psw, balance)
    return account


def get_user():
    # if user is new or old account
    choice = input('1. New\n2. Old\n>_')
    if choice == '1':
        return new_account()
    return old_account()
