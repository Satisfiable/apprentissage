"""
liste = [1,2,3,4,5]
# print(dir(liste))

iterator = iter(liste)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) StopIteration
"""

"""
liste = [1,2,3,4,5]

for i in liste:
    print(i)

def iter_fonksiyonu(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print("Stop Iteration Error")
            break

iterable = [1,2,3,4,5]
iter_fonksiyonu(iterable)
"""

class Kumanda():
    def __init__(self, kanal_listesi):
        self.kanal_listesi = kanal_listesi
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        if (self.index < len(self.kanal_listesi)):
            return self.kanal_listesi[self.index]
        else:
            raise StopIteration("Stop Iteration Error")

kumanda = Kumanda(["Kanal d","Trt","Atv","Fox","Bloomberg"])
iterator = iter(kumanda)

"""
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
"""

for i in kumanda:
    print(i)

        



