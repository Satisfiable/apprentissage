from user_operations import *
from library_operations import *
import time, random
import sqlite3
import socket

class Test():

    def main(self):
        
        user = User_Operations()

        text = """
        Kullanıcı işlemleri

        1. Giriş yap
        2. Kullanıcı adımı veya şifremi unuttum
        3. Kayıt ol
        4. Yardım iste
        Çıkış: Q\n"""

        count1 = 0
        while True:

            is_blocked = user.block_ip_address(False)

            if (is_blocked == True):
                print("\nIp adresiniz engellendiği için giriş yapamazsınız! 2 Saat içinde tekrar deneyebilirsiniz.")
                return

            print(text)
            answer = input("Bir işlem seçin: ")

            if (answer == "1" or answer.lower() == "giriş yap"):
                print("\nİşlem: Giriş yap")

                username = user.login()

                fetch_query = "SELECT * FROM User_Informations WHERE Username = ?"

                user.cursor.execute(fetch_query, (username,))
                account_informations = user.cursor.fetchall()

                if (len(account_informations) != 0):
                    print("Merhaba {}!".format(account_informations[0][2]))
                    library = Library_Operations()
                    library.visual_library()
                    return

            elif (answer == "2" or answer.lower() == "kullanıcı adımı veya şifremi unuttum" or answer.lower() == "kullanıcı adımı unuttum" or answer.lower() == "şifremi unuttum"):
                print("\nİşlem: Kullanıcı adımı veya şifremi unuttum\n")
                
                if (answer == "2" or answer.lower() == "kullanıcı adımı veya şifremi unuttum"):
                    
                    count2 = 0
                    while True:
                        if (count2 == 0):
                            answer = input("Kullanıcı adınızı mı yoksa şifrenizi mi unuttunuz? ")
                        elif (count2 == 3):
                            print("3 kez geçersiz işlem yaptınız! Kullanıcı adı veya şifre sıfırlama talebi sonlandırılıyor...")
                            break
                        else:
                            answer = input("\nAşağıdaki bilgilerden hangisini unuttunuz:\nKullanıcı adı\nŞifre\n\nSeçiminiz: ")

                        if ("kullanıcı adı" in answer.lower() and (len(answer.split()) == 2 or (len(answer.split()) == 3))):
                            user.reset_username()
                            return
                        elif ("şifre" in answer.lower() or "parola" in answer.lower() and (len(answer.split()) == 1 or len(answer.split()) == 2)):
                            user.reset_password()
                            return
                        else:
                            count2 += 1
                elif (answer.lower() == "kullanıcı adımı unuttum"):
                    user.reset_username()
                elif (answer.lower() == "şifremi unuttum"):
                    user.reset_password()
            elif (answer == "3" or answer.lower() == "kayıt ol"):
                print("\nİşlem: Kayıt ol")
                user.register()
            elif (answer == "4" or answer.lower() == "yardım iste"):
                print("\nİşlem: Yardım iste")
                user.help()
            elif (answer.lower() == "q"):
                print("Çıkış yapılıyor... Görüşmek üzere!")
                return
            else:
                count1 += 1

                if (count1 == 5):
                    print("5 kez geçersiz işlem yaptınız! Kullanıcı işlemleri sonlandırılıyor...")
                    return
                else:
                    print("\nGeçersiz işlem!")
    
if __name__ == "__main__":
    test = Test()
    test.main()