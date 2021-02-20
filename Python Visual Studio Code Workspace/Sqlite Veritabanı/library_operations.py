from visual_library import *
import time

class Library_Operations():

    def visual_library(self):
        text = """
Kütüphane uygulamasına hoşgeldiniz...

Yönetici işlemleri:
1. Kitapları listele
2. Kitap sorgula
3. Kitap ekle
4. Kitap sil
5. Baskı yükselt
Çıkış: Q"""

        kütüphane = Kütüphane()

        count = 0
        while True:
            print(text)

            answer = input("\nBir işlem seçin: ")

            if (answer.lower() == "q"):
                print("Uygulamadan çıkış yapılıyor...")
                break
            elif (answer== "1" or answer.lower() == "kitapları listele"):
                kütüphane.kitaplari_goster()

            elif (answer== "2" or answer.lower() == "kitap sorgula"):

                kitap = input("Aradığınız kitabın ismini girin: ")
                print("{} isimli kitap aranıyor...".format(kitap[0].upper() + kitap[1:]))
                time.sleep(2)
                
                kütüphane.kitap_sorgula(kitap)

            elif (answer== "3" or answer.lower() == "kitap ekle"):
                
                kitap_isim = input("\nKitabın ismi: ")
                kitap_yazar = input("Kitabın yazarı: ")
                kitap_tür = input("Kitabın türü: ")
                kitap_yayınevi = input("Kitabın yayınevi: ")
                kitap_baskı = input("Kitabın baskısı: ")

                kitap = Kitap(kitap_isim, kitap_yazar, kitap_tür, kitap_yayınevi, kitap_baskı)
                kütüphane.kitap_ekle(kitap)

            elif (answer== "4" or answer.lower() == "kitap sil"):
                
                kitap_isim = input("Silmek istediğiniz kitabın ismi: ")
                kütüphane.kitap_sil(kitap_isim)

            elif (answer== "5" or answer.lower() == "baskı yükselt"):
                
                kitap_isim = input("Baskısını yükseltmek istediğiniz kitabın ismi: ")
                kütüphane.baski_yukselt(kitap_isim)
                
            else:
                count += 1

                if (count >= 3):
                    print("3 kez geçersiz işlem yaptınız! Uygulamadan çıkış yapılıyor...")
                    break
                else:
                    print("Geçersiz işlem!")