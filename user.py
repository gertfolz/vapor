import db

class User:
    def __init__ (self, name, password):
        self.name = name
        self.password = password

    def printUser(self):
        print(self.name+'\n'+self.password)
        print(f'{self.name}\n{self.password}')
        
    def createAccount(self):
        userData = db.getUser(self.name)
        print(userData)
        if not userData:
            db.insertUser(self)
            print("Account created\n")
        else:
            print("User already exists :(\n")
