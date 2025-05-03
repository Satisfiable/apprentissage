"""
def ana_fonksiyon(işlem_adı):

    def toplama(*args):

        toplam = 0
        for i in args:
            toplam += i

        return toplam

    def çarpma(*args):

        çarpım = 1
        for i in args:
            çarpım *= i

        return çarpım

    if (işlem_adı == "toplama"):
        return toplama
    elif (işlem_adı == "çarpma"):
        return çarpma
    else:
        return 0

fonk = ana_fonksiyon("toplama")
print(fonk)
toplam = fonk(1,2,3,4,5,6,7,8,9,10)
print(toplam)

fonk2 = ana_fonksiyon("çarpma")
print(fonk2)
çarpım = fonk2(1,2,3,4,5)
print(çarpım)
"""

def toplama(*args):
    
    toplam = 0
    for i in args:
        toplam += i

    return toplam

def çarpma(*args):

    çarpım = 1
    for i in args:
        çarpım *= i

    return çarpım

def ekrana_bastırma(*args):
    return args

def ana_fonksiyon(func1, func2, func3, işlem_adı):

    if (işlem_adı == "toplama"):
        print(func1(1,2,3,4,5,6,7))
    elif (işlem_adı == "çarpma"):
        print(func2(5,4,3,2,1))
    elif (işlem_adı == "ekrana bastırma"):
        x = func3("Merhaba", "Python")

        for i in x:
            print(i)

    else:
        print("Geçersiz işlem adı!")

ana_fonksiyon(toplama, çarpma, ekrana_bastırma, "çarpma")
