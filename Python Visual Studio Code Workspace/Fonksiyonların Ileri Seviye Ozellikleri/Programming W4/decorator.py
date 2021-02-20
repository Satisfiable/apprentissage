
def my_decorator(func):

    def wrapper(sayılar):

        mükemmel_sayı = list()

        for i in sayılar:
            toplam = 0
            for j in sayılar:

                if (i % j == 0):
                    toplam += j

            print(toplam)
            if (toplam == i):
                mükemmel_sayı.append(i)

        func(sayılar)
        print(mükemmel_sayı)
        print(func.__name__ + " fonksiyonu bitti!")
    
    return wrapper

@my_decorator
def asal_sayılar(sayılar):

    asal_sayı = list()

    for i in sayılar:
        count = 0
        for j in sayılar:

            if (i % j == 0):
                count += 1

        if (count == 2):
            asal_sayı.append(i)
    
    print(asal_sayı)

asal_sayılar(range(1,1000))

