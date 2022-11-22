
def addtake(user, choice):
    amount = float(input('Amount:\n>_'))
    balance = float(user.balance)

    if choice == '1':
        balance += amount

    if choice == '2':
        balance -= amount

    user.balance = str(balance)


def main_prompt(user):
    while True:
        print(f'*User: {user.name}\t\t*Balance: {user.balance} Euro')
        choice = input('\n1.Add\n2.Take\nq = Quit\n>_')

        if choice == '1':
            addtake(user, choice)

        if choice == '2':
            addtake(user, choice)

        if choice == 'q':
            break

    return user
