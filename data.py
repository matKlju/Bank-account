from user_creation import *


def save_data(user):
    user_data = {'Name': user.name, 'Balance': user.balance}

    with open(user.name, 'w') as account:
        account.write(str(user_data))
        print('Data saved!')


def read_data(name):
    while True:
        try:
            with open(name, 'r') as account:
                a = account.read()

            name = a[0]
            balance = a[1]

            account = User(name, balance)
            # return User Object
            return account

        except FileNotFoundError:
            print('No account!')
            continue
