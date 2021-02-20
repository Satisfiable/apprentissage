def ekstra(function):
    def wrapper(sayılar):

        çiftler_toplamı = 0
        çift_sayılar = 0
        tekler_toplamı = 0
        tek_sayılar = 0

        for sayı in sayılar:

            if (sayı % 2 == 0):
                çiftler_toplamı += sayı
                çift_sayılar += 1
            else:
                tekler_toplamı += sayı
                tek_sayılar += 1

        print("Tek sayıların ortalaması: ", (tekler_toplamı / tek_sayılar))
        print("Çift sayıların ortalaması: ", (çiftler_toplamı / çift_sayılar))

        function(sayılar)
    
    return wrapper

@ekstra
def ortalama_hesapla(sayılar):
    
    toplam = 0

    for sayı in sayılar:
        toplam += sayı

    print("Sayıların genel ortalaması: ", (toplam / len(sayılar)))

ortalama_hesapla(range(100))