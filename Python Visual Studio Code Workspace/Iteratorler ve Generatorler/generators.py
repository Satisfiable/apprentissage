def kareleri_al():
    for i in range(1,6):
        yield i ** 2

generator = kareleri_al()
print(generator)

iterator = iter(generator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))

liste = [i ** 3 for i in range(5)] # List Comprehension
print(liste)

generator2 = (i ** 3 for i in range(5)) 
print(generator2)

iterator2 = iter(generator2)

print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))

def çarpım_tablosu():
    for i in range(1, 11):
        for j in range(1, 11):
            yield "{0} x {1} = {2}".format(i, j, i * j)

for i in çarpım_tablosu():
    print(i)