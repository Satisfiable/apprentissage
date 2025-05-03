class Dosya():

    def __init__(self):

        text_path = "C:/Users/USER/Desktop/Programming W4/Ileri Seviye Veri Tipleri/Kodlama Egzersizi/metin.txt"
        with open(text_path, "r", encoding = "utf-8") as file:

            dosya_içeriği = file.read()
            kelimeler = dosya_içeriği.split()
            self.sade_kelimeler = list()
            
            for i in kelimeler:
                
                i = i.strip("\n")
                i = i.strip(".")
                i = i.strip(",")
                i = i.strip(" ")

                self.sade_kelimeler.append(i)

            for i in self.sade_kelimeler:
                print(i)

    def tum_kelimeler(self):

        kelimeler_kümesi = set()

        for i in self.sade_kelimeler:
            kelimeler_kümesi.add(i)

        print("Tüm benzersiz kelimeler:")
        for i in kelimeler_kümesi:
            print(i)
            print("*******************")


    def kelime_frekansı(self):

        kelime_sözlük = dict()

        for i in self.sade_kelimeler:

            if (i in kelime_sözlük):
                kelime_sözlük[i] += 1
            else:
                kelime_sözlük[i] = 1

        for kelime, sayı in kelime_sözlük.items():

            print("{} kelimesi {} defa geçiyor".format(kelime, sayı))

dosya = Dosya()
dosya.tum_kelimeler()
dosya.kelime_frekansı()