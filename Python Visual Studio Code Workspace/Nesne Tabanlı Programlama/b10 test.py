class Bilgisayar():

    def __init__(self, marka, işletim_sistemi, işlemci, bellek_miktarı, ekran_kartı):
        self.marka = marka
        self.işletim_sistemi = işletim_sistemi
        self.işlemci = işlemci
        self.bellek_miktarı = bellek_miktarı
        self.ekran_kartı = ekran_kartı

    def __str__(self):
        return "Bilgisayarın;\nMarkası: {}\nİşletim sistemi: {}\nİşlemcisi {}\nBellek miktarı: {}\nEkran kartı: {}\n".format(self.marka, self.işletim_sistemi, self.işlemci, self.bellek_miktarı, self.ekran_kartı)

    def __len__(self):
        return 0

    def __del__(self):
        print("Bilgisayar sistemden siliniyor...")

    def bilgi_degistir(self, degisken_ismi, deger):

        if (degisken_ismi.lower() == "marka"):
            self.marka = deger
        elif (degisken_ismi.lower() == "işletim sistemi"):
            self.işletim_sistemi = deger
        elif (degisken_ismi.lower() == "işlemci"):
            self.işlemci = deger
        elif (degisken_ismi.lower() == "bellek miktarı"):
            self.bellek_miktarı = deger
        elif (degisken_ismi.lower() == "ekran kartı"):
            self.ekran_kartı = deger
        else:
            print("Geçersiz değişken ismi girdiniz!")
            return

    def bilgi_ogren(self, degisken_ismi, deger):

        if (degisken_ismi.lower() == "marka"):
            return self.marka
        elif (degisken_ismi.lower() == "işletim sistemi"):
            return self.işletim_sistemi
        elif (degisken_ismi.lower() == "işlemci"):
            return self.işlemci
        elif (degisken_ismi.lower() == "bellek miktarı"):
            return self.işletim_sistemi
        elif (degisken_ismi.lower() == "ekran kartı"):
            return self.ekran_kartı
        else:
            print("Geçersiz değişken ismi girdiniz!")
            return 0

bilgisayar = Bilgisayar("Casper Nirvana", "Windows 10", "Intel i5 3370", "8", "Geforce GT 630M")

x = bilgisayar.__str__
y = bilgisayar.__len__
print(x, y, sep = "\n\n")

degisken_ismi = input("\nDeğişken ismi giriniz: ")
yeni_deger = input("Yeni değer: ")
bilgisayar.bilgi_degistir(degisken_ismi, yeni_deger)

degisken_ismi2 = input("\nDeğişken ismi giriniz: ")
deger = input("Yeni değer: ")
bilgisayar.bilgi_ogren(degisken_ismi, deger)