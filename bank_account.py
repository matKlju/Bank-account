"""

new attempt for to simulate a bank account

To_do:
    check if file already exists
    

"""
from sys import exit as sys_exit
from pyinputplus import inputMenu
from user_account import get_account, save_account


def main_menu():
    """Main loop and choices"""

    account = get_account()

    while True:

        account.display_account()
        choice = inputMenu(['Withdraw', 'Deposit', 'Quit'], numbered=True)

        if choice == 'Withdraw':
            account.withdraw()

        elif choice == 'Deposit':
            account.deposit()

        else:
            save_account(account)
            sys_exit()


if __name__ == '__main__':
    main_menu()
