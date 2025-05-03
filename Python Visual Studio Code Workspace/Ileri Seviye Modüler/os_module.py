import os
from datetime import datetime

print(os.getcwd())

"""
os.chdir("C:\\Users\\User\\Desktop")
print(os.getcwd())

for i in os.listdir():
    print(i)
"""

# os.mkdir("Klasor1")
# os.makedirs("Klasor2/Klasor3")

# os.rmdir("Klasor1")
# os.removedirs("Klasor2/Klasor3")

# os.rename("metin.txt", "text.txt")

print(os.stat("text.txt").st_mtime)
print(datetime.fromtimestamp(os.stat("text.txt").st_mtime))

for i in os.walk("C:\\Users\\User\\Desktop"):
    print(i)

for klasor_yolu, klasor_isimleri, dosya_isimleri in os.walk("C:\\Users\\User\\Desktop"):
    print("Klasör yolu:", klasor_yolu)
    print("Klasör ismi:", klasor_isimleri)
    print("Dosya ismi:", dosya_isimleri)
    print("*********************************************")

for klasor_yolu, klasor_isimleri, dosya_isimleri in os.walk("C:\\Users\\User\\Desktop"):
    for i in dosya_isimleri:
        if (i.endswith(".txt")):
            print(i)