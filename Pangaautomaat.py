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

# Old calculator
#
# pin = " "
# balance = 3000.00
# attempt = 3
# while pin != "2308" and attempt > 0:
#     print("Sisesta PIN-kood:")
#     print("Katseid jäänud: " + str(attempt))
#     pin = getpass()
#     attempt -= 1
#
#
# if attempt == 0 and pin != "2308":
#     print("Katsete arv otsas! Oled v2lja logitud")
#     exit()
#
# if pin == "2308":
#     print("Sisenesid pangaautomaati! Sinu saldo on "  + str(balance) + " € ")
#
#
# def user_option():
#     user_input = input("Võta raha = a , Sisesta raha = b , Välju = c : ")
#     return user_input
#
#
# option = user_option()
#
# while option != "c":
#     while option == "a":
#         quantity = abs(float(input("Palju soovid välja võtta ?: ")))
#
#         if option == "a" and quantity > balance:
#             print("Kontol pole piisavalt raha")
#             print(f"Kontojääk:{str(round(balance, 2))}€")
#             option = user_option()
#         if option == "a" and quantity <=  balance:
#             balance -= quantity
#             print(f"Võetud: {str(round(quantity, 2))}€")
#             print("Kontojääk: {str(round(balance, 2))}€")
#             option = user_option()
#
#     while option == "b":
#         quantity = abs(float(input("Palju soovid lisada ?: ")))
#         if option == "b":
#             balance += quantity
#             print("Lisatud: " + str(round(quantity, 2)) + " € ")
#             print("Kontojääk:  "  + str(round(balance, 2)) + " € ")
#             option = user_option()
# print("Oled välja logitud!")
# exit()
