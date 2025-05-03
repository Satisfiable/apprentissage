x = "python".upper()
print(x)

x = "PYTHON".lower()
print(x)

x = "PythOn".upper()
print(x)

x = "PythOn".lower()
print(x)

y = "Herkes ana baba bacı gardaş".replace("a","o")
print(y)

y = "Kunduz".replace("duz","zun")
print(y)

y = "Python Programlama Dili".replace(" ","-")
print(y)

z = "Python".startswith("py")
print(z)

z = "Python".startswith("Py")
print(z)

z = "Python".endswith("on")
print(z)

z = "Python".endswith("az")
print(z)

liste = "Python Programlama Dili".split(" ")
print(liste)

liste = "Python-Php-Java-C-Javascript".split("-")
print(liste)

x = "                   python                          ".strip()
print(x)

x = "                   python                  y       ".lstrip()
print(x)

x = "                   python                          ".rstrip()
print(x)

x = ">>>>>>>>>>>>>>>>>>>>>>>>Mustafa>>>>>>>>>>>>>>>>>>>>>>>>>>".strip(">")
print(x)

liste = ["21","02","2014"]
x = "/".join(liste)
print(x)

liste = ["T","B","M","M"]
x = ".".join(liste)
print(x)

x = "ada kapısı yandan çarklı".count("a")
print(x)

x = "ada kapısı yandan çarklı".count(" ")
print(x)

x = "ada kapısı yandan çarklı".count("a", 2)
print(x)

y = "araba".find("a")
print(y)

y = "araba".find("s")
print(y)

y = "araba".rfind("a")
print(y)

y = "araba".rfind("s")
print(y)