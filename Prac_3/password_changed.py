def main():
    minlength=4
    password=get_password("gimme password")
    while password<4:
        password=input("please enter a password longer than 4: ")
    for i in password:
        print("*",end="")


def get_password(message):
    passwords=input(message)
    return passwords
