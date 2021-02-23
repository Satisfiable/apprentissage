import sqlite3
import time
import random

"""
Örnek özellikler;

1. Şarkı İsmi 
2. Sanatçı
3. Albüm
4. Prodüksiyon Şirketi
5. Şarkı Süresi

Örnek Metodlar;

1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
2. Şarkı Ekle
3. Şarkı Sil
"""

class Şarkı():

    def __init__(self, şarkı_ismi = "", sanatçı = "", albüm = "", prodüksiyon_şirketi = "", şarkı_süresi = ""):
        self.şarkı_ismi = şarkı_ismi
        self.sanatçı = sanatçı
        self.albüm = albüm
        self.prodüksiyon_şirketi = prodüksiyon_şirketi
        self.şarkı_süresi = şarkı_süresi

        self.connect_database()

    def connect_database(self):

        self.connection = sqlite3.connect("Şarkı.db")
        self.cursor = self.connection.cursor()
        
        create_query = "CREATE TABLE IF NOT EXISTS Şarkı_Listesi (Şarkı_İsmi TEXT, Sanatçı TEXT, Albüm TEXT, Prodüksiyon_Şirketi TEXT, Şarkı_Süresi TEXT)"
        self.cursor.execute(create_query)
        self.connection.commit()

    def __str__(self):
        return "\nŞarkı ismi: {}\nSanatçı: {}\nAlbüm: {}\nProdüksiyon Şirketi: {}\nŞarkı süresi: {}\n".format(self.şarkı_ismi, self.sanatçı, self.albüm, self.prodüksiyon_şirketi, self.şarkı_süresi)

    def __len__(self):
        return self.şarkı_süresi

    def __del__(self, şarkı_ismi):

        select_query = "SELECT Şarkı_İsmi FROM Şarkı_Listesi WHERE Şarkı_İsmi = ?"
        self.cursor.execute(select_query, (şarkı_ismi,))
        informations = self.cursor.fetchall()

        if (len(informations) == 0):
            print("\n{} isimli şarkı bulunamadı!".format(şarkı_ismi))
            return
        else:
            print("\nŞarkı siliniyor...")
            time.sleep(1.2)

            delete_query = "DELETE FROM Şarkı_Listesi WHERE Şarkı_İsmi = ?"
            self.cursor.execute(delete_query, (şarkı_ismi,))
            self.connection.commit()

            print("Şarkı başarıyla silindi!")

    def total_song_time(self):

        select_query = "SELECT Şarkı_Süresi FROM Şarkı_Listesi"
        self.cursor.execute(select_query)
        informations = self.cursor.fetchall()

        if (len(informations) == 0):
            print("Veritabanında şarkı bulunmuyor!")
            return
        else:

            try:
                total_time = 0
                for i in range(0, len(informations)):

                    total_time += int(informations[i][0])

                return total_time
            except Exception as e:
                print("Beklenmeyen bir hata oluştu! Hata kodu: " + str(e))

    def şarkı_ekle(self, şarkı):
        
        try:
            insert_query = "INSERT INTO Şarkı_Listesi VALUES (?,?,?,?,?)"
            self.cursor.execute(insert_query, (self.şarkı_ismi, self.sanatçı, self.albüm, self.prodüksiyon_şirketi, self.şarkı_süresi))
            self.connection.commit()

            print("Şarkı başarıyla eklendi!")
        except Exception as e:
            print("Beklenmeyen bir hata oluştu! Hata kodu: " + str(e))

    def şarkı_sil(self, şarkı_ismi):
        self.__del__(şarkı_ismi)

    def şarkı_güncelle(self, şarkı_ismi, alan, new_value):
        
        try:
            update_query = "UPDATE Şarkı_Listesi SET {} = ? WHERE = ?".format(alan)
            self.cursor.execute(update_query, (new_value, şarkı_ismi))
            self.connection.commit()

            print("Şarkı güncellendi!")
        except Exception as e:
            print("Beklenmeyen bir hata oluştu! Hata kodu: " + str(e))

    def şarkı_listele(self, annotation, şarkı_ismi = ""):

        if (annotation == True):
            select_query = "SELECT * FROM Şarkı_Listesi"
            self.cursor.execute(select_query)
            informations = self.cursor.fetchall()

            if (len(informations) == 0):
                print("\nVeritabanında şarkı bulunmuyor!")
                return
            else:
                
                count = 0
                for i in range(0, len(informations)):
                    şarkı = Şarkı(informations[i][0], informations[i][1], informations[i][2], informations[i][3], informations[i][4])
                    count += 1

                    print("\nŞarkı {}:".format(count))
                    print(str(şarkı))
        else:
            select_query = "SELECT * FROM Şarkı_Listesi WHERE Şarkı_İsmi = ?"
            self.cursor.execute(select_query, (şarkı_ismi,))
            informations = self.cursor.fetchall()

            if (len(informations) == 0):
                print("\nAradığınız şarkı bulunamadı!")
                return
            else:
                
                for i in range(0, len(informations)):
                    şarkı = Şarkı(informations[i][0], informations[i][1], informations[i][2], informations[i][3], informations[i][4])
                    print(str(şarkı))