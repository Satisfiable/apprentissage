import sqlite3

class Kitap():

    def __init__(self, isim, yazar, tür, yayınevi, baskı):
        self.isim = isim
        self.yazar = yazar
        self.tür = tür
        self.yayınevi = yayınevi
        self.baskı = baskı

    def __str__(self):
        return "\nKitabın;\n\tİsmi: {}\n\tYazarı: {}\n\tTürü: {}\n\tYayınevi: {}\n\tBaskı: {}\n".format(self.isim, self.yazar, self.tür, self.yayınevi, self.baskı)

class Kütüphane():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("kütüphane.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS Kitaplar (İsim TEXT, Yazar TEXT, Tür TEXT, Yayınevi TEXT, Baskı INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitaplari_goster(self):

        sorgu = "SELECT * FROM Kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Kütüphanede kitap bulunmuyor!")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4])
                print(kitap)

    def kitap_sorgula(self, isim):

        sorgu = "SELECT * FROM Kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu, (isim,))
        kitap_bilgileri = self.cursor.fetchall()

        if (len(kitap_bilgileri) == 0):
            print("Aradığınız kitap bulunamadı!")
        else:
            for i in range(0, len(kitap)):
                kitap = Kitap(kitap_bilgileri[i][0], kitap_bilgileri[i][1], kitap_bilgileri[i][2], kitap_bilgileri[i][3], kitap_bilgileri[i][4])
                print(kitap)

    def kitap_ekle(self, kitap):

        sorgu = "INSERT INTO Kitaplar VALUES (?,?,?,?,?)"
        self.cursor.execute(sorgu, (kitap.isim, kitap.yazar, kitap.tür, kitap.yayınevi, kitap.baskı))
        self.baglanti.commit()

    def kitap_sil(self, isim):

        sorgu = "DELETE FROM Kitaplar WHERE İsim = ?"
        self.cursor.execute(sorgu, (isim,))
        self.baglanti.commit()
    
    def baski_yukselt(self, isim):

        sorgu1 = "SELECT * FROM Kitaplar WHERE İsim = ?"
        self.cursor.execute(sorgu1, (isim,))
        kitap_bilgileri = self.cursor.fetchall()

        if (len(kitap_bilgileri) == 0):
            print(isim, "isminde bir kitap bulunmuyor!")
        else:
            for i in range(0, len(kitap_bilgileri)):
                baskı = kitap_bilgileri[i][4]
                baskı += 1

                sorgu2 = "UPDATE Kitaplar SET Baskı = ? WHERE İsim = ?"
                self.cursor.execute(sorgu2, (baskı, isim))
                self.baglanti.commit()