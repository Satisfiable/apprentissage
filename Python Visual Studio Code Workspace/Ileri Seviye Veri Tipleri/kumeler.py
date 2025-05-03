x = set()
print(type(x))

x = {3,4,7,5,6}
print(x)

liste = [1,1,2,2,2,3,3,3,3,3]
x = set(liste)
print(x)

x = set("Python Programlama Dili")
print(x)

x = {"Python", "Php", "Python"}
print(x)

x = {"Python", "Java", "Ruby", "Flask"}
for i in x:
    print(i)

liste = list(x)
print(liste)
print(liste[0])

x = {1,2,3}
x.add(5)
print(x)

x.add(3)
print(x)

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

print(küme1.difference(küme2))
print(küme2.difference(küme1))

print(küme1, küme2, sep = "\n")
küme1.difference_update(küme2)
print(küme1)

x = {1,2,3,4,5,6}
x.discard(2)
print(x)

x.discard(10)
print(x)

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

x = küme1.intersection(küme2)
print(x)

küme1.intersection_update(küme2)
print(küme1)

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme3 = {30,40,50}

print(küme1.isdisjoint(küme2))
print(küme1.isdisjoint(küme3))

küme1 = {1,2,3}
küme2 = {1,2,3,4}
küme3 = {5,6,7}

x = küme1.issubset(küme2)
print(x)

x = küme1.issubset(küme3)
print(x)

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

print(küme1.union(küme2))

küme1.update(küme2)
print(küme1)


