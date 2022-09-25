import Auth

def start():
    while True:
        begin=int(input("Do you have login? \nPlease Enter 1(No) or 2(Yes)\n"))
        if (begin==1):

            Auth.Register.login()
        elif (begin==2):
            Auth.Auth.login()



if __name__ == "__main__":
    # program starts
    a = Auth()
    start()
