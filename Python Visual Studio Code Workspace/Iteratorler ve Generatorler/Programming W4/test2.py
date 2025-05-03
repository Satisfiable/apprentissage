def numbers(first_number = 1, last_number = 1000):

    if (not (last_number > first_number)) or (first_number < 1):
        raise ValueError("Bir takım hatalar oluştu! Doğru değerleri girdiğinizden emin olun.")

    for i in range(first_number, last_number):
        count = 0

        for j in range(first_number, last_number):

            if (i % j == 0):
                count += 1

        if (count == 2):
            yield i

for i in numbers(1, 1000):
    print(i)

        