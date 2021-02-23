def function(value):

    if (value % 2 == 0):
        return value
    else:
        raise ValueError("Girdiğiniz sayı bir tek sayı!")

x = int(input("Çift sayı: "))
value = function(x)

liste = [1,2,3,4,5,6,7,8,9,10]

for i in range(0, len(liste)):
    if (liste[i] % 2 == 0):
        print(liste[i])