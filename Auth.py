import json
import hashlib


class User:
    def __init__(self, username, name, surname, age, password, password_confirm):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        self.password = password
        self.password_confirm = password_confirm
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
        return self.password

    @property
    def get_password_confirm(self):
        return self.password_confirm


class Auth:
    def __init__(self):
        self.user = None

    def signIN(self, username, name, surname, age, password, password_confirm):
        if password != password_confirm:
            raise ValueError('Passwords not equall')
        self.user = User(username, name, surname, age, self.hash_password(password),
                         self.hash_password(password_confirm))
        self.save()

        print(self.user)

    @staticmethod
    def hash_password(password):
        txt = hashlib.sha512(password.encode('utf-8'))
        hashed_password = txt.hexdigest()
        return hashed_password

    def save(self):
        with open(f'database/{self.user.username}.json', 'w', encoding='utf-8') as f:
            json.dump(self.user.__dict__, f, indent=4)

    def login(self, username, password):
        with open(f'database/{username}.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            if data.get('password') == self.hash_password(password):
                print(' Success')
            ch = input('Exchange password?(1) \nExit(0) ')

            if ch == '1':
                new_password = input('Your new password')
                self.change_password(username, password, new_password)

    def change_password(self, password, new_password):
        with open(f'database/{username}.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            ##searching old password then change it
            if data.get('password') == self.hash_password(password):
                data['password'] = self.hash_password(new_password)
                with open(f'database/{username}.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4)
