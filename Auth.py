import json
import hashlib

class User:
    def __init__(self, username, name,surname,age, password):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        self.password = password
        self.is_active = False
    @property
    def get_username(self):
        return self.username

    @property
    def get_name(self):
        return self.name
    @property
    def get_surname(self):
        return self.get_surname

    @property
    def get_password(self):
        return data.password

class Register :
    def login(self):
        username= input("Username:\n")

        name=input("Name:\n")
        surname=input("Surname:\n")
        try:
            age=int(input("Your age:\n"))
        except:
          print("Not available data. Try again")
          Register.login()

        password= input("Password:\n")
        password_confirm= input("Confirm your password:\n")
        if (password!=password_confirm):
            print("passwords are not the same!\n Try again!")
            Register.login()
        else:
            print("Success!")

        with open(database.json/{self.u.username}.json, 'w', encoding='utf-8') as database:
            json.dump(user_data, database, indent=4)

class Auth:
    def login(self):
        username =input("Enter username;\n")
        password= input("Enter password:\n")