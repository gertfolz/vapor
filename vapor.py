from user import User

OPTIONS = "12"

# get option
option = input("1 - Sign in\n2 - Sign up\n")
while option not in OPTIONS:
    option = input("1 - Sign in\n2 - Sign up\n")

# get user info
username = input("Type your username:\n")
password = input("Type your password:\n")
user = User(username, password)

# execute option
if option == "1":
    user.login()
elif option == "2":
    user.createAccount()
