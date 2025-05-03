import sqlite3

connection = sqlite3.connect("my_database.db")

cursor = connection.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Çalışanlar (Numara INT, İsim TEXT, Soyisim TEXT, Alanı DATE)")
    connection.commit()

def veri_ekle1():
    cursor.execute("INSERT INTO Çalışanlar VALUES (172, 'Maeve', 'Mll', 'Web Programming')")
    connection.commit()

def veri_ekle2(numara, isim, soyisim, alan):
    cursor.execute("INSERT INTO Çalışanlar VALUES (?,?,?,?)", (numara, isim, soyisim, alan))
    connection.commit()

def veri_al1():
    cursor.execute("SELECT * FROM Çalışanlar")
    veriler = cursor.fetchall()

    for i in veriler:
        print(i)

def veri_al2():
    cursor.execute("SELECT İsim, Soyisim FROM Çalışanlar")
    veriler = cursor.fetchall()

    for i in veriler:
        print(i)

def veri_al3(numara):
    cursor.execute("SELECT * FROM Çalışanlar WHERE numara = ?", (numara,))
    veriler = cursor.fetchall()

    for i in veriler:
        print(i)

def veri_guncelle(numara, alan):
    cursor.execute("UPDATE Çalışanlar SET alanı = ? WHERE numara = ?", (alan, numara))
    connection.commit()

def veri_sil(numara):
    cursor.execute("DELETE FROM Çalışanlar WHERE numara = ?", (numara,))
    connection.commit()

tablo_olustur()

veri_ekle1()

connection.close()