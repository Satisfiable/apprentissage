import sys

"""
name = input("Adınız: ")
surname = input("Soyadınız: ")

sys.exit()

age = input("Yaşınız: ")
"""

sys.stderr.write("Bu bir hata mesajıdır!\n")
sys.stderr.flush()

sys.stdout.write("Bu normal bir mesajdır.\n")

for i in sys.argv:
    print(i)

print(sys.argv)

def kok_bulma(a,b,c):
    delta = b ** 2  - 4 * a * c

    if (delta < 0):
        print("Reel Kök Yok.")

    else:
        x1 = (-b - delta ** 0.5) / (2*a)
        x2 = (-b + delta ** 0.5) / (2*a)
        return (x1,x2)

if (len(sys.argv) == 4):
    sys.stdout.write("Kök bulma: " + str(kok_bulma(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))))
else:
    sys.stderr.write("Hata! Değerleri lütfen doğru girin.")
    sys.stderr.flush()