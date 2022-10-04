


pin = " "
ballance = 3000.00
attempt = 3
while pin != "2308" and attempt > 0:
    print("Sisesta PIN-kood:")
    print("Katseid jäänud: " + str(attempt))
    pin = input()
    attempt -= 1


if attempt == 0 and pin != "2308":
    print("Katsete arv otsas! Oled v2lja logitud")
    exit()

if pin == "2308":
    print("Sisenesid pangaautomaati! Sinu saldo on "  + str(ballance) + " € ")


def user_option():
    user_input = input("Võta raha = a , Sisesta raha = b , Välju = c : ")
    return user_input


option = user_option()

while option != "c":
    while option == "a":
        quantity = abs(float(input("Palju soovid välja võtta ?: ")))
        if option == "a" and quantity > ballance:
            print("Kontol pole piisavalt raha")
            print("Kontojääk: "  + str(round(ballance, 2)) + " € ")
            option = user_option()
        if option == "a" and quantity <=  ballance:
            ballance -= quantity
            print("Võetud: " + str(round(quantity, 2)) + " € ")
            print("Kontojääk: "  + str(round(ballance, 2)) + " € ")
            option = user_option()
    while option == "b":
        quantity = abs(float(input("Palju soovid lisada ?: ")))
        if option == "b":
            ballance += quantity
            print("Lisatud: " + str(round(quantity, 2)) + " € ")
            print("Kontojääk:  "  + str(round(ballance, 2)) + " € ")
            option = user_option()
print("Oled välja logitud!")
exit()


# 375.73 + 5.42
