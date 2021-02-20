def fonksiyon1(*args):

    for i in args:
        print(i)

fonksiyon1("Python", 1, 2, 3)

def fonksiyon2(isim, *args):

    print("İsim: " + str(isim))

    for i in args:
        print(i)

fonksiyon2("Berkay", 0, -1, -2, -3, -4)

def fonksiyon3(*isimler):

    for i in isimler:
        print(i)

fonksiyon3("Berkay", "Maive", "Scofield")

def fonksiyon4(**kwargs):

    for (i,j) in kwargs.items():
        print(str(i) + ": " + str(j))

fonksiyon4(isim = "Berkay", yas = 16, alan = "Web Development")

def fonksiyon5(*args, **kwargs):

    for i in args:
        print(i)

    print("----------------")

    for (i,j) in kwargs.items():
        print(str(i) + ": " + str(j))

    print("\n")

fonksiyon5(4,5,6,7,8,9, isim = "Berkay", yas = 16, alan = "Web Development")

def selamla(isim):
    print("Selamlar", isim)

selamla("Maive")
print(selamla)

merhaba = selamla
print(merhaba)

merhaba("Scofield")

del selamla

try:
    print(selamla)
except NameError:
    print("[Hata] selamla değişkeni henüz tanımlanmamış!")

print(merhaba)
merhaba("Scofield")

def function1():

    def function2():
        print("Küçük fonksiyondan herkese merhaba!")

    function2()
    print("Büyük fonksiyondan herkese merhaba!")

function1()

try:
    function2()
except NameError:
    print("[Hata] function2 fonksiyonu henüz tanımlanmamış!")

def myfunction(*args):

    def toplama(args):

        toplam = 0

        for i in args:
            toplam += i

        return toplam

    print(toplama(args))

myfunction(3,4,5,6,7,8,9,0)
