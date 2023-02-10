"""

new attempt for to simulate a bank account

"""
import pyinputplus as pyip
from user_account import *


def start_menu():
    choice = pyip.inputMenu(['New account', 'Old account', 'Quit'], numbered=True)

    if choice == 'New account':
        account = new_account()         # create new account
    elif choice == 'Old account':
        account = load_account()
    else:
        quit()

    return account


def main_menu(account):
    while True:
        account.display_account()
        choice = pyip.inputMenu(['Withdraw', 'Deposit', 'Quit'], numbered=True)

        if choice == 'Withdraw':
            account.withdraw()  # create new account
        elif choice == 'Deposit':
            account.deposit()
        else:
            save_account(account)
            quit()


if __name__ == '__main__':
    user = start_menu()
    main_menu(user)
