def kelime_frekansı():
    text = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

    letter_dict = dict()

    for i in text:

        if (i in letter_dict):
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1

    for x,y in letter_dict.items():
        print("Text'in içinde {0} harfi {1} defa geçiyor.".format(x, y))
        print("$")

def long_text():

    text_path = "C:/Users/USER/Desktop/Programming W4/Ileri Seviye Veri Tipleri/Programming W4/şiir.txt"

    with open(text_path, "r", encoding = "utf-8") as file:

        file_content = file.read()
        file_content = file_content.split()

        my_string = ""

        for i in file_content:
            if (i[0].isupper()):
                my_string += i[0]

        print(my_string)

def find_true_mail():

    text_path = "C:/Users/USER/Desktop/Programming W4/Ileri Seviye Veri Tipleri/Programming W4/mailler.txt"

    with open(text_path, "r", encoding = "utf-8") as file:

        file_content = file.read()
        file_content = file_content.split()

        for i in file_content:
            if (i.endswith("@gmail.com")):
                print(i)

find_true_mail()


