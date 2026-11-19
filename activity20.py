from getpass import getpass

user = "princess carla"
passwords = "carla"

is_Login = False

while is_Login == False:

    user = input( " please enter your username --->  ")
    password = getpass(" please enter your password --->  ")

    if user == user and password == passwords:
        print(" ACCESS GRANTED")
        is_Login = True

    else:
        print(" ACCESS DENIED ")
        is_Login = False