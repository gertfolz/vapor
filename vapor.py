from user import User


option = input("1 - Sign in\n2 - Sign up\n")
username = input("Type your username: \n")
password = input("Type your password: \n")
newUser = User(username, password)
if option == "2":
    newUser.createAccount()







