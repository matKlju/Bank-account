
def new_password():
    while True:
        password = input('Password:\n>_')
        repeat = input('Repeat password:\n>_')

        if repeat == password:
            return password

        print("Passwords don't match")