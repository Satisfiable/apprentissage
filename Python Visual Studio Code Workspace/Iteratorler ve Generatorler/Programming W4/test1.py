class Kareler():

    def __init__(self, max):
        self.max = max
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):

        if (self.number <= self.max):
            result = self.number ** 2
            self.number += 1

            return result
        else:
            self.number = 0
            raise StopIteration("This is a Stop Iteration Error!")

kareler = Kareler(7)

iterator = iter(kareler)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))