f = open("fisier.in", "r")
L = f.read()
f.close()
lst = []
cuvant = input("Cuvant: ")
sep = ".,-?!"
for x in sep:
    L = L.replace(x, " ")
v = "Cuvintele sunt: "
for x in L.split():
    if(set(x) == set(cuvant)):
        lst.append(x)

s = ", ".join(lst)
s = v+s+"."
print(s)

