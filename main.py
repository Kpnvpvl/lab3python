from Auth import Auth


def start(a):
    # while False:
    try:
        begin = int(input("Do you have login? \nPlease Enter 1(No) or 2(Yes)\n"))
        if (begin == 1):
            username = input('Username: ')
            name = input("Name:")
            surname = input("Surname: ")
            age = input("Age: ")
            password = input("Password: ")
            password_confirm = input("Password_confirm: ")
            a.signIN(username, name, surname, age, password, password_confirm)

        elif (begin == 2):
            username = input('Username:')
            password = input('Password:')
            a.login(username, password)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    # program starts here
    a = Auth()
    start(a)
