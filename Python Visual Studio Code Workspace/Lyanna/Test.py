from Database import Database

"""
Veri tabanı işlemleri:

[1] Veri sorgula
[2] Veri ekle
[3] Veri güncelle
[4] Veri sil
[5] Statement ekle
[6] Statement güncelle
[7] Statement sil
"""

def main():

    database = Database()
    result = database.connect_database()

    if (result == False):
        return

    compass = """\nVeri tabanı işlemleri:\n\n[1] Veri sorgula\n[2] Veri ekle\n[3] Veri güncelle\n[4] Veri sil\n[5] Statement ekle\n[6] Statement güncelle\n[7] Statement sil\n"""

    while True:
        print(compass)
        choice = input("Bir işlem seçmelisiniz: ")

        if (choice == "1" or choice.lower() == "veri sorgula"):

            error_count = 0
            while True:
                if (error_count == 0):
                    print("\nİşlem: Veri sorgula")
                    date = input("Aradığınız verinin kaydedildiği tarihi girin: ")
                elif (error_count > 0):
                    date = input("Aradığınız verinin kaydedildiği tarihi girin: (Örn: 05.12.2019) ")

                split_date = date.split(".")

                access = False
                for i in split_date:
                    if not (i.isnumeric):
                        access = True
                        break

                if (access == True):
                    error_count += 1
                    continue

                if (len(date) == 10 and len(split_date) == 3):
                    data = database.search_data(date)
                    
                    if (len(data) == 0):
                        print("\n{} Tarihli veri bulunamadı!".format(date))
                        break
                    else:
                        for i in data:
                            print(data)
                else:
                    error_count += 1

if __name__ == "__main__":
    main()
                    

            


