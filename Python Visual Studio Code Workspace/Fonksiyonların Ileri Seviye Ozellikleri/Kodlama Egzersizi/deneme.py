import sqlite3
import time
import random

def reset_password(function):

    def wrapper():

        random_code = 513635
        confirmation_code = function()

        if (random_code == confirmation_code):
            print("\nDoğrulama kodu doğru!")
        else:
            print("\nDoğrulama kodu yanlış!")
    
    return wrapper

@reset_password
def reset_account_password():

    informations = [["satisfying432@gmail.com", "7se2Te3en"]]

    email = input("\nHesabınıza tanımlı e-posta adresini girin: ")

    access = False
    for i in informations:
        if (i[0].lower() != email.lower()):
            continue
        else:
            access = True
            username_email = i
    
    if (access == True):

        username_email = email.split("@")
        username_email = username_email[0]

        censored_email = username_email[0:2]

        for i in range(0, len(username_email)):
            if (i > 1 and i < len(username_email) - 1):
                censored_email += "*"
            elif (i == len(username_email) - 1):
                censored_email += username_email[-1]
            
        censored_email += ("@" + username_email[1])

        print("{} adlı e-posta adresine bir doğrulama kodu gönderildi.".format(censored_email))

        confirmation_code = int(input("\nDoğrulama kodunu girin: "))
        return confirmation_code
            

reset_account_password()