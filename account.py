import os
import os.path

class Account():
        def __init__(self, username, password):
            self.username = username
            self.password = password

if os.path.isfile("username.txt") == True:
    f = open("username.txt", "r")
    print("It seems you already made an account.", "Hello " + (f.read()) + ".")
    reset = input("Would you like to reset password and username? (Y/N): ")
    if reset == "Y":
        f.close()
        f = open("password.txt", "r")
        current = input("Enter current password: ")
        if current == f.read():
            f.close()
            Accountnew = Account(input("Insert username: "), input("Insert password: "))

            f = open("username.txt", "w")
            f.write(Accountnew.username)
            f.close()

            f = open("password.txt", "w")
            f.write(Accountnew.password)
            f.close()
        
        else:
            f.close()
            print("The password you have entered is incorrect.")

    else:
        print("Alright, see ya then", (f.read()) + ".")
        f.close()
else:

    Accountnew = Account(input("Insert username: "), input("Insert password: "))

    f = open("username.txt", "w")
    f.write(Accountnew.username)
    f.close()

    f = open("password.txt", "w")
    f.write(Accountnew.password)
    f.close()