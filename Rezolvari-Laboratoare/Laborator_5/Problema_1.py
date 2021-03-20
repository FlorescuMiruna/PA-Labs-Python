f = open("tis.txt")

timpi = f.read()
timpi = timpi.split()
print(timpi)
lista = []
for i in range(0,len(timpi)):
    lista.append((int(timpi[i]),i))

print(lista)
def cmp(l):
    return l[0]

def functie(l):
    medie = 0
    s = 0
    for x in l:
        medie += s+x[0]
        s += x[0]
        print(x[0]," ",x[1])

    medie = medie/len(l)
    print("Timpul mediu de asteptare este: ",medie)

functie(lista)

lista.sort(key = cmp)

functie(lista)