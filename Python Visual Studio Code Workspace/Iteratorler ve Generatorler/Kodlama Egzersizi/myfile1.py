class kuvvet3():

    def __init__(self, max = 0):
        self.max = max
        self.kuvvet = 0

    def __iter__(self):
        return self

    def __next__(self):

        if (self.kuvvet <= self.max):

            result = 3 ** self.kuvvet
            self.kuvvet += 1

            return result
        else:
            self.kuvvet = 0
            raise StopIteration("This is a Stop Iteration error.")

kuvvet = kuvvet3(5)

for i in kuvvet:
    print(i)

for i in kuvvet:
    print(i)

"""
iterator = iter(kuvvet)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))
"""
