import db

class User:
    def __init__ (self, name, password):
        self.name = name
        self.password = password

    # print user info
    def printUser(self):
        print(self.name+'\n'+self.password)
        print(f'{self.name}\n{self.password}')
    
    # create user account
    def createAccount(self):
        userData = db.getUser(self.name)
        print(userData)
        if not userData:
            db.insertUser(self)
            print("Account created")
        else:
            print("User already exists :(")
    
    # log user in
    def login(self):
        userData = db.getUser(self.name)
        if not userData:
            print("User not found :(")
            return
        password = userData[0][1]
        if self.password != password:
            print("Wrong password :(")
            return
        print("Logged in! :)")
