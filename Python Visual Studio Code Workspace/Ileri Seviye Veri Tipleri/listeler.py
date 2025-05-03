liste = [1,2,3,4,5,6,7]
liste.append("Python")
print(liste)

liste.append(100)
print(liste)

liste1 = [1,2,3,4,5,6,7]
liste2 = [10,11,12]

liste1.extend(liste2)
print(liste1)

liste = [1,2,3,4,5,6,7,8,9]
liste.insert(2, "Python")
print(liste)

liste.insert(0, 0)
print(liste)

liste.insert(len(liste), 99)
print(liste)

liste = [1,2,3,4,5,6,7]
x = liste.pop()
print(x)

x = liste.pop(0)
print(x)

liste = ["Python","Php","Java","C"]
liste.remove("Python")
print(liste)

liste = [1,2,3,4,3,3,5,6,7,8,9]
x = liste.index(3)
print(x)

x = liste.index(3, 3)
print(x)

liste = [1,2,3,4,5,6,1,1,1,1,1,1,1,1,8]
x = liste.count(1)
print(x)

x = liste.count(10)
print(x)

liste = [12,-2,3,1,34,100]
liste.sort()
print(liste)

liste2 = ["Python","Php","C","Java"]
liste2.sort()
print(liste2)

liste = [12,-2,3,1,34,100]
liste.sort(reverse = True)
print(liste)

liste2 = ["Python","Php","C","Java"]
liste2.sort(reverse = True)
print(liste2)