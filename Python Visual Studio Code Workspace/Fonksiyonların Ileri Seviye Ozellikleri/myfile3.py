import time

"""
def kareleri_hesapla(sayılar):
    sonuç = list()
    baslama = time.time()

    for i in sayılar:
        sonuç.append(i ** 2)

    bitis = time.time()
    print("Bu fonksiyon " + str(bitis - baslama) + " saniye sürdü.")
    
    return sonuç

def küpleri_hesapla(sayılar):
    sonuç = list()
    baslama = time.time()

    for i in sayılar:
        sonuç.append(i ** 3)

    bitis = time.time()
    print("Bu fonksiyon " + str(bitis - baslama) + " saniye sürdü.")

    return sonuç

kareleri_hesapla(range(100000))
küpleri_hesapla(range(100000))
"""

def zaman_hesapla(function):
    def wrapper(sayılar):

        baslama = time.time()
        sonuç = function(sayılar)
        bitis = time.time()

        print(function.__name__ + " " + str(bitis - baslama) + " saniye sürdü.")
        return sonuç

    return wrapper

@zaman_hesapla
def kareleri_hesapla(sayılar):
    sonuç = list()
    baslama = time.time()

    for i in sayılar:
        sonuç.append(i ** 2)

    bitis = time.time()
    
    return sonuç

@zaman_hesapla
def küpleri_hesapla(sayılar):
    sonuç = list()
    baslama = time.time()

    for i in sayılar:
        sonuç.append(i ** 3)

    bitis = time.time()

    return sonuç

kareleri_hesapla(range(100000))
küpleri_hesapla(range(100000))
