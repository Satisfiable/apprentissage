import sqlite3
import time
import random
import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class User_Operations():

    system_prefix = "[Sistem]"
    error_prefix = "[Hata]"

    def __init__(self):
        
        self.connect_database()

    def connect_database(self):

        try:
            self.connection = sqlite3.connect("kütüphane.db")
            self.cursor = self.connection.cursor()

            create_table_query = "CREATE TABLE IF NOT EXISTS User_Informations (Username TEXT, Password TEXT, Name TEXT, Surname TEXT, Email TEXT, Birthdate TEXT, Last_Seen TEXT, Ip_Address TEXT)"
            self.cursor.execute(create_table_query)
            self.connection.commit()

        except Exception as e:
            print("\n{} Beklenmeyen bir hata oluştu! Veri tabanına bağlanılamadı! Hata kodu: ".format(self.error_prefix) + str(e))
    
    def close_database(self):

        self.connection.close()

    def login(self):

        incorrect_entry = 0
        
        while True:
            while True:
                username = input("\nKullanıcı adı: ")

                if not (username.strip()):
                    print("Bir kullanıcı adı girmek zorundasınız!")
                    continue
                else:
                    break

            if (username.lower() == "q"):
                print("\n{} Çıkış yapılıyor...".format(self.system_prefix))
                time.sleep(2)
                return

            if (username.lower() == "y"):
                answer = input("Kullanıcı adınızı mı yoksa şifrenizi mi sıfırlayacaksınız: ")

                if ("kullanıcı adı" in answer.lower() and (len(answer.split()) == 2 or (len(answer.split)) == 3)):
                    self.reset_username()
                    return

                elif ("şifre" in answer.lower() or "parola" in answer.lower() and (len(answer.split()) == 1 or len(answer.split()) == 2)):
                    self.reset_password()
                    return
                else:
                    print("\n{} Geçersiz işlem!".format(self.error_prefix))
                    continue

            while True:
                password = input("Şifre: ")

                if not (password.strip()):
                    print("Bir şifre girmek zorundasınız!")
                    continue
                else:
                    break

            if (password.lower() == "q"):
                print("\n{} Çıkış yapılıyor...".format(self.system_prefix))
                time.sleep(2)
                return
            
            if (password.lower() == "y"):
                answer = input("\nKullanıcı adınızı mı yoksa şifrenizi mi sıfırlayacaksınız: ")

                if ("kullanıcı adı" in answer.lower() and (len(answer.split()) == 2 or (len(answer.split)) == 3)):
                    self.reset_username()
                    return

                elif ("şifre" in answer.lower() or "parola" in answer.lower() and (len(answer.split()) == 1 or len(answer.split()) == 2)):
                    self.reset_password()
                    return
                else:
                    print("\n{} Geçersiz işlem!".format(self.error_prefix))
                    continue

            login_query = "SELECT Username FROM User_Informations WHERE Username = ? and Password = ?"
            self.cursor.execute(login_query, (username, password))
            account_informations = self.cursor.fetchall()
        
            if (len(account_informations) == 0):
                incorrect_entry += 1

                if (incorrect_entry  <= 3):
                    print("\nKullanıcı adınız veya şifreniz yanlış! Tekrar deneyin ya da 'Y' tuşuna basarak sıfırlayın.")
                    continue
                else:
                    print("\nKullanıcı adınızı veya şifrenizi 4 kez hatalı girdiniz. Ip adresiniz geçici olarak engelleniyor...")
                    self.block_ip_address(True)
                    return
            else:

                last_seen = time.strftime("%H:%M | %d.%m.%Y")

                update_query = "UPDATE User_Informations SET Last_Seen = ? WHERE Username = ?"
                self.cursor.execute(update_query, (last_seen, username))
                self.connection.commit()

                return username
        
    def reset_username(self):

        email = input("\nHesabınıza tanımlı e-posta adresini girin: ")

        search_query = "SELECT Username FROM User_Informations WHERE Email = ?"
        self.cursor.execute(search_query, (email,))
        informations = self.cursor.fetchall()

        if (len(informations) == 0):
            print("E-posta adresi bulunamadı!")
            return
        else:
            result, random_code = self.send_mail(email, "Kullanıcı adı hatırlatma talebi", True)

            if (result == False):
                return

            username_email = email.split("@")
            surname_email = username_email[1]
            username_email = username_email[0]

            censored_email = username_email[0:2]

            for i in range(0, len(username_email)):
                if (i > 1 and i < len(username_email) - 1):
                    censored_email += "*"
                elif (i == len(username_email) - 1):
                    censored_email += username_email[-1]
            
            censored_email += ("@" + surname_email)

            print("{} adlı e-posta adresine bir doğrulama kodu gönderildi.".format(censored_email))                    

            try:
                confirmation_code = int(input("\nDoğrulama kodunu girin: "))

                if (random_code == confirmation_code):
                    count = 0
                    while True:
                        print("\nİşlemler:\n1. Kullanıcı adını değiştir.\n2. Mevcut kullanıcı adımı e-posta adresime gönder.")
                        answer = input("\nBir işlem seçin: ")

                        if (answer == "1" or ("kullanıcı adını değiştir" in answer and len(answer.split()) == 3)):
                            count = 0
                            while True:
                                new_username = input("\nYeni kullanıcı adınızı girin: ")

                                all_symbols = "_abcçdefgğhiıjklmnoöpqrsştuüvwxyzABCÇDEFGHİIJKLMNOÖPQRSŞTUÜVWXYZ0123456789"

                                special_symbols_boolean = False
                                for i in range(0, len(new_username)):
                                    if not (new_username[i] in all_symbols):
                                        special_symbols_boolean = True
                                        break

                                if (special_symbols_boolean == True):
                                    print("\nKullanıcı adınız özel karakter içermemeli!")
                                    continue

                                if ((len(new_username) < 6) or len(new_username) > 30):
                                    print("\nKullanıcı adınız en az 6, en fazla 30 karakterden oluşabilir.")
                                    continue
                                
                                select_query = "SELECT Username FROM User_Informations WHERE Username = ?"
                                self.cursor.execute(select_query, (new_username,))
                                informations = self.cursor.fetchall()

                                if (len(informations) == 0):

                                    new_username_again = input("\nYeni kullanıcı adınızı tekrar girin: ")

                                    if (new_username == new_username_again):
                                        add_query = "UPDATE User_Informations SET Username = ? WHERE Email = ?"
                                        self.cursor.execute(add_query, (new_username, email))
                                        self.connection.commit()
                                        print("\nKullanıcı adınız başarıyla değiştirildi!")
                                        return
                                    else:
                                        count += 1

                                        if (count == 3):
                                            print("\n{} 3 Kez geçersiz işlem yaptınız. Kullanıcı adı hatırlama talebi sonlandırılıyor...".format(self.error_prefix))
                                            return
                                        else:
                                            print("\nKullanıcı adları eşleşmiyor!")
                                else:
                                    print("\nBu kullanıcı adı alınmış. Başka bir tane deneyin.")

                        elif (answer == "2" or ("mevcut kullanıcı adımı e-posta adresime gönder" in answer and len(answer.split()) == 6)):
                            result = self.send_mail(email, "Kullanıcı adı hatırlatma talebi", False) 

                            if (result == True):
                                print("\nHesabınıza tanımlı mevcut kullanıcı adınız e-posta adresinize gönderildi.")
                                return
                
                        else:
                            count += 1
                            if (count == 3):
                                print("\n{} 3 Kez geçersiz işlem yaptınız. Kullanıcı adı hatırlama talebi sonlandırılıyor...".format(self.error_prefix))
                                return
                            else:
                                print("\n{} Geçersiz işlem!".format(self.error_prefix))
                else:
                    print("\nDoğrulma kodu yanlış! Kullanıcı adı hatırlama talebi sonlandırılıyor...")
                    return
            except ValueError:
                print("\n{} Doğrulama kodunu hatalı girdiniz!".format(self.error_prefix))
            except Exception as e:
                ("\n{} Beklenmeyen bir hata oluştu! kullanıcı adı sıfırlanamadı! Hata kodu: ".format(self.error_prefix) + str(e))

    def reset_password(self):

        email = input("\nHesabınıza tanımlı e-posta adresini girin: ")

        search_query = "SELECT Username FROM User_Informations WHERE Email = ?"
        self.cursor.execute(search_query, (email,))
        informations = self.cursor.fetchall()

        if (len(informations) == 0):
            print("E-posta adresi bulunamadı!")
        else:
            result, random_code = self.send_mail(email, "Şifre hatırlatma talebi", True)

            if (result == False):
                return

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

            try:
                confirmation_code = int(input("\nDoğrulama kodunu girin: "))

                if (random_code == confirmation_code):
                    count = 0
                    while True:
                        new_password = input("\nYeni şifrenizi girin: ")

                        all_symbols = ["abcçdefgğhiıjklmnoöpqrsştuüvwxyzABCÇDEFGHİIJKLMNOÖPQRSŞTUÜVWXYZ0123456789", "abcçdefgğhiıjklmnoöpqrsştuüvwxyz", "ABCÇDEFGĞHİIJKLMNOÖPQRSŞTUÜVWXYZ", "0123456789"]

                        banned_symbols_boolean = False
                        for i in range(0, len(new_password)):
                            if not (new_password[i] in all_symbols[0]):
                                banned_symbols_boolean = True
                                break
                        
                        if (banned_symbols_boolean == True):
                            print("\nŞifreniz özel karakter içermemeli!")
                            continue

                        lower_letters_boolean = False
                        for i in range(0, len(all_symbols[1])):
                            if (all_symbols[1][i] in new_password):
                                lower_letters_boolean = True
                                break

                        if (lower_letters_boolean == False):
                            print("\nŞifreniz en az bir küçük harf içermeli!")
                            continue

                        upper_letters_boolean = False
                        for i in range(0, len(all_symbols[2])):
                            if (all_symbols[2][i] in new_password):
                                upper_letters_boolean = True
                                break

                        if (upper_letters_boolean == False):
                            print("\nŞifreniz en az bir büyük harf içermeli!")
                            continue

                        numbers_boolean = False
                        for i in range(0, len(all_symbols[3])):
                            if (all_symbols[3][i] in new_password):
                                numbers_boolean = True
                                break

                        if (numbers_boolean == False):
                            print("\nŞifreniz en az bir rakam içermeli!")
                            continue

                        if (len(new_password) < 8):
                            print("\nŞifreniz en az 8 karakterden oluşabilir.")
                            continue

                        new_password_again = input("\nYeni şifrenizi tekrar girin: ")

                        if (new_password == new_password_again):
                            add_query = "UPDATE User_Informations SET Password = ? WHERE Email = ?"
                            self.cursor.execute(add_query, (new_password, email))
                            self.connection.commit()
                            print("\nŞifreniz başarıyla değiştirildi!")
                            return
                        else:
                            count += 1

                            if (count == 3):
                                print("\n{} 3 Kez geçersiz işlem yaptınız. Şifre hatırlama talebi sonlandırılıyor...".format(self.error_prefix))
                                return
                            else:
                                print("\nŞifreler eşleşmiyor!")
                else:
                    print("\nDoğrulma kodu yanlış! Şifre hatırlama talebi sonlandırılıyor...")
                    return
            except ValueError:
                print("\n{} Doğrulama kodunu hatalı girdiniz!".format(self.error_prefix))
            except Exception as e:
                ("\n{} Beklenmeyen bir hata oluştu! Şifre sıfırlanamadı! Hata kodu: ".format(self.error_prefix) + str(e))

    def send_mail(self, email, subject, annotation):

        message = MIMEMultipart()
        message["From"] = "Satisfying432@gmail.com"
        message["To"] = email
        message["Subject"] = subject
        
        if ("kullanıcı adı" in subject.lower()):
            subject_smaller = "kullanıcı adı"
        elif ("şifre" in subject.lower()):
            subject_smaller = "şifre" 

        username_email = email.split("@")
        username_email = username_email[0]

        if (annotation == True):
        
            while (1):
                random_code = random.randint(220000, 880000)

                if (random_code % 10 == 0 or random_code % 100 == 0 or random_code % 1000 == 0 or random_code % 10000 == 0 or random_code & 100000 == 0):
                    continue
                else:
                    break
            
            contains = "Sevgili {0},\nVisual Library {1} hatırlatma servisini kullandığınız için bu maili aldınız. Eğer bu talebi gerçekleştirmiş olan sizseniz lütfen aşağıdaki doğrulama kodunu kullanın.\n\nDoğrulama kodu: {2}\n\nAlzheimer kullanıcı adı sıfırlama servisi sorumlusu\n\nBerkay Yavuz".format(username_email, subject_smaller, random_code)

        else:

            query = "SELECT Username FROM User_Informations WHERE Email = ?"
            self.cursor.execute(query, (email))
            username = self.cursor.fetchall()
            username = username[0]

            contains = "Sevgili {0},\nVisual Library {1} hatırlatma servisini kullandığınız için bu maili aldınız. Hesabınıza tanımlı kullanıcı adını aşağıdadır.\n\nKullanıcı adınız: {2}\n\nAlzheimer kullanıcı adı sıfırlama servisi sorumlusu\n\nBerkay Yavuz".format(username_email, subject_smaller, username)

        message_body = MIMEText(contains, "Plain")
        message.attach(message_body)

        try:
            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(message["From"], "7se2Te3en")
            mail.sendmail(message["From"], message["To"], message.as_string())
            mail.close()

            if (annotation == True):
                return True, random_code
            else:
                return True
        except Exception as e:

            print("\n{} Beklenmeyen bir hata oluştu! Mail gönderilemedi! Hata kodu: ".format(self.error_prefix) + str(e))

            if (annotation == True):
                return False, 0
            else:
                return False
                
    def register(self):

        # Username, Password, Name , Surname , Email, Birthdate, Last_Seen, Ip_Address
        try:
            while True:
                while True:
                    name = input("\nAdınız: ")

                    if not (name.strip()):
                        print("Adınızı girmek zorundasınız!")
                        continue
                    else:
                        break
                
                while True:
                    surname = input("Soyadınız: ")

                    if not (surname.strip()):
                        print("Soyadınızı girmek zorundasınız!\n")
                        continue
                    else:
                        break

                while True:
                    username = input("\nKullanıcı adı: ")

                    if not (username.strip()):
                        print("Bir kullanıcı adı girmek zorundasınız!")
                        continue

                    all_symbols = "_abcçdefgğhiıjklmnoöpqrsştuüvwxyzABCÇDEFGHİIJKLMNOÖPQRSŞTUÜVWXYZ0123456789"

                    special_symbols_boolean = False
                    for i in range(0, len(username)):
                        if not (username[i] in all_symbols):
                            special_symbols_boolean = True
                            break

                    if (special_symbols_boolean == True):
                        print("\nKullanıcı adınız özel karakter içermemeli!")
                        continue

                    if (len(username) < 6 or len(username) > 30):
                        print("\nKullanıcı adınız en az 6, en fazla 30 karakterden oluşabilir.")
                        continue
                    
                    select_query = "SELECT Username FROM User_Informations WHERE Username = ?"
                    self.cursor.execute(select_query, (username,))
                    informations = self.cursor.fetchall()

                    if (len(informations) == 0):
                        break
                    else:
                        print("\nBu kullanıcı adı alınmış. Başka bir tane deneyin.")

                count = 0
                while True:
                    password = input("\nŞifre: ")

                    if not (password.strip()):
                        print("Bir şifre girmek zorundasınız!")
                        continue

                    all_symbols = ["abcçdefgğhiıjklmnoöpqrsştuüvwxyzABCÇDEFGHİIJKLMNOÖPQRSŞTUÜVWXYZ0123456789", "abcçdefgğhiıjklmnoöpqrsştuüvwxyz", "ABCÇDEFGĞHİIJKLMNOÖPQRSŞTUÜVWXYZ", "0123456789"]

                    banned_symbols_boolean = False
                    for i in range(0, len(password)):
                        if not (password[i] in all_symbols[0]):
                            banned_symbols_boolean = True
                            break
                    
                    if (banned_symbols_boolean == True):
                        print("\nŞifreniz özel karakter içermemeli!")
                        continue

                    lower_letters_boolean = False
                    for i in range(0, len(all_symbols[1])):
                        if (all_symbols[1][i] in password):
                            lower_letters_boolean = True
                            break

                    if (lower_letters_boolean == False):
                        print("\nŞifreniz en az bir küçük harf içermeli!")
                        continue

                    upper_letters_boolean = False
                    for i in range(0, len(all_symbols[2])):
                        if (all_symbols[2][i] in password):
                            upper_letters_boolean = True
                            break

                    if (upper_letters_boolean == False):
                        print("\nŞifreniz en az bir büyük harf içermeli!")
                        continue

                    numbers_boolean = False
                    for i in range(0, len(all_symbols[3])):
                        if (all_symbols[3][i] in password):
                            numbers_boolean = True
                            break

                    if (numbers_boolean == False):
                        print("\nŞifreniz en az bir rakam içermeli!")
                        continue

                    if (len(password) < 8):
                        print("\nŞifreniz en az 8 karakterden oluşabilir!")
                        continue

                    password_again = input("\nŞifrenizi tekrar girin: ")

                    if (password == password_again):
                        break
                    else:
                        count += 1

                        if (count == 3):
                            print("\n{} 3 Kez geçersiz işlem yaptınız. Kayıt olma talebi sonlandırılıyor...".format(self.error_prefix))
                            return
                        else:
                            print("\nŞifreler eşleşmiyor!")

                while True:
                    email = input("\nE-posta adresiniz: ")

                    if not (email.strip()):
                        print("E-posta adresinizi girmek zorundasınız!")
                        continue

                    if not ("@" in email):
                        print("\nGeçersiz e-posta adresi. E-posta adresiniz şuna benzer bir şekilde olmalıdır: example@gmail.com")
                        continue

                    email_split = email.split("@")

                    if (len(email_split[0]) < 6 or len(email_split[0]) > 30):
                        print("\nGeçersiz e-posta adresi. E-posta adresinizin kullanıcı adı en az 6, en fazla 30 karakterden oluşmalıdır.")
                        continue
                    else:
                        break

                while True:
                    birthdate = input("Doğum tarihiniz: (Örneğin 18.01.2004) ")

                    birthdate_split = birthdate.split(".")
                    
                    isnt_numeric_boolean = False
                    for i in range(0, len(birthdate_split)):
                        if not (birthdate_split[i].isnumeric):
                            isnt_numeric_boolean = True
                            break

                    if (isnt_numeric_boolean == True or len(birthdate_split) != 3):
                        print("\nGeçersiz doğum tarihi. Doğum tarihiniz şuna benzer bir şekilde olmalıdır: 18.01.2004")
                        continue
                    else:
                        break

                last_seen = ""

                hostname = socket.gethostname()
                ip_address = socket.gethostbyname(hostname)

                insert_query = "INSERT INTO User_Informations VALUES (?,?,?,?,?,?,?,?)"
                insert_data = (username, password, name, surname, email, birthdate, last_seen, ip_address)
                self.cursor.execute(insert_query, insert_data)
                self.connection.commit()
            
                print("\nKayıt başarıyla tamamlandı!")
                return

        except Exception as e:
            ("\n{} Beklenmeyen bir hata oluştu! Şifre sıfırlanamadı! Hata kodu: ".format(self.error_prefix) + str(e))

    def block_ip_address(self, block):

        create_query = "CREATE TABLE IF NOT EXISTS Blocked_Ip_Addresses (Ip_Address TEXT, Blocked_Time TEXT)"
        self.cursor.execute(create_query)
        self.connection.commit()

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        if (block == True):

            blocked_time = time.strftime("%d.%m.%Y.%X")

            blocked_time_array = blocked_time.split(".")

            blocked_time_array[:3] = [[blocked_time_array[0], blocked_time_array[1], blocked_time_array[2]]]
            blocked_time_array[1] = blocked_time_array[1].split(":")

            block_query = "INSERT INTO Blocked_Ip_Addresses VALUES (?,?)"
            self.cursor.execute(block_query, (ip_address, str(blocked_time_array)))
            self.connection.commit()
        else:

            control_query = "SELECT * FROM Blocked_Ip_Addresses WHERE Ip_Address = ?"
            self.cursor.execute(control_query, (ip_address,))
            informations = self.cursor.fetchall()

            if (len(informations) == 0):
                return False
            else:
                now = time.strftime("%d.%m.%Y.%X")

                now_array = now.split(".")

                now_array[:3] = [[now_array[0], now_array[1], now_array[2]]]
                now_array[1] = now_array[1].split(":")

                blocked_time = informations[0][1]
                ns = []

                for i in blocked_time:

                    if (i.isnumeric()):
                        ns += [i]

                date_information = [ns[0] + ns[1], ns[2] + ns[3], ns[4] + ns[5] + ns[6] + ns[7]]
                time_information = [ns[-6] + ns[-5], ns[-4] + ns[-3], ns[-2] + ns[-1]]

                blocked_time = [date_information, time_information]

                count = 0
                for i in range(0, len(blocked_time[0])):
                    if (now_array[0][i] == blocked_time[0][i]):
                        count += 1
                    else:
                        break

                if (count == 3):
                    if (int(now_array[1][0]) - int(blocked_time[1][0]) >= 2):
                        delete_query = "DELETE FROM Blocked_Ip_Addresses WHERE Ip_Address = ?"
                        self.cursor.execute(delete_query, (ip_address,))
                        self.connection.commit()
                        return False
                    else:
                        return True
                else:
                    delete_query = "DELETE FROM Blocked_Ip_Addresses WHERE Ip_Address = ?"
                    self.cursor.execute(delete_query, (ip_address,))
                    self.connection.commit()
                    return False

    def help(self):

        try:
            subject = input("\nKonu: ")
            contain = input("Mesajınız: ")
            importance_level = int(input("Önem seviyesi: (1-5) "))

            while not (importance_level >= 1 and importance_level <= 5):
                importance_level = int(input("\nYardım talebiniz için 1 ile 5 arasında bir önem seviyesi girin: "))

            email = input("Size ulaşabileceğimiz bir e-posta adresi: ")

            sent_time = time.strftime("%d.%m.%Y | %H:%M")

            create_table_query = "CREATE TABLE IF NOT EXISTS Help_List (Importance_Level INT, Subject TEXT, Message TEXT, Email TEXT, Time TEXT)"
            self.cursor.execute(create_table_query)
            self.connection.commit()

            insert_query = "INSERT INTO Help_List VALUES (?,?,?,?,?)"
            self.cursor.execute(insert_query, (importance_level, subject, contain, email, sent_time))
            self.connection.commit()

            print("\nYardım talebinize en yakın zaman dönüş yapacağız.")
        
        except ValueError:
            print("\n{} Önem seviyesini hatalı girdiniz!".format(self.error_prefix))
        except Exception as e:
            print("\n{} Beklenmeyen bir hata oluştu!  Yardım talebi oluşturulamadı! Hata kodu: ".format(self.error_prefix) + str(e))