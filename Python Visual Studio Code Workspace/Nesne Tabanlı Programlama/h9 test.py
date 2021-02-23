class Hayvan():

    def __init__(self, isim, tur, ayak_sayisi, yas):
        self.isim = isim
        self.tur = tur
        self.ayak_sayisi = ayak_sayisi
        self.yas = yas

    def yemek_ye(self):
        print("{} yemek yiyiyor!".format(self.isim))
    
    def uyan(self):
        print("{} uyanıyor...".format(self.isim))

class Kopek(Hayvan):
    
    def __init__(self, isim, tur, ayak_sayisi, yas, dis_sayisi):
        super().__init__(isim, tur, ayak_sayisi, yas)
        self.dis_sayisi = dis_sayisi

    def havla(self):
        print("{} havlıyor!".format(self.isim))

    def saldir(self):
        print("{} saldırıyor...".format(self.isim))

class Kus(Hayvan):

    def __init__(self, isim, tur, ayak_sayisi, yas, kanat_sayisi, havada_kalabilme_suresi):
        super().__init__(isim, tur, ayak_sayisi, yas)
        self.kanat_sayisi = kanat_sayisi
        self.havada_kalabilme_suresi = havada_kalabilme_suresi

    def fly(self):
        print("{}, {} kanadıyla uçuyor...".format(self.isim, self.kanat_sayisi))

    def rekor(self):
        print("{}, {} dakika havada kalabilme süresini {} dakika yapıyor.".format(self.isim, self.havada_kalabilme_suresi, self.havada_kalabilme_suresi + 2))
        self.havada_kalabilme_suresi = self.havada_kalabilme_suresi + 2

class At(Hayvan):
    
    
    def __init__(self, isim, tur, ayak_sayisi, yas, hiz, renk):
        super().__init__(isim, tur, ayak_sayisi, yas)
        self.hiz = hiz
        self.yas = yas

    def hizlan(self):
        print("{}, {} hızını {} arttırarak hızlanıyor...".format(self.isim, self.hiz, 2.1))


hayvan = Hayvan("Mor", "İnek", 4, 7)
hayvan.uyan()
hayvan.yemek_ye()

kopek = Kopek("Pamuk", "Köpek", 4, 7, 16)
kopek.uyan()
kopek.havla()
kopek.saldir()

kus = Kus("Işık", "Kuş", 2, 3, 2, 17.2)
kus.fly()
kus.rekor()
kus.yemek_ye()

at = At("Formula", "At", 4, 6, 81.1, "Beyaz")
at.hizlan()
at.uyan()