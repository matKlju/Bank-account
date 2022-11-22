from user_creation import *
from data import *
from main_prompt import *


def main():
    while True:
        user = get_user()  # Decide if new or old user
        user = main_prompt(user)  # user argument to main_prompt module, returns modified user account
        save_data(user)  # save data after done
        print('Bye!!')
        quit()


if __name__ == '__main__':
    main()
