f = open("obiecte.txt","r")
n = int(f.readline())
obiecte = []
for i in range(0,n):
    val,greutate= f.readline().split()
    obiecte.append((int(val),int(greutate)))

greutate_maxima = int(f.readline())


def cmpRaportGreutateValoare(t):
    return -(t[0]/t[1])

def fractie(a, b):
    m = a
    n = b
    while b:
        c = a % b
        a = b
        b = c

    return "(" + str(m//a) + "/" + str(n//a) + ")"

obiecte.sort(key = cmpRaportGreutateValoare)
print(obiecte)

sir1 = "greutate:\n" + str(greutate_maxima) + " = "
sir2 = "valoare obiecte din rucsac:\n"
i = 0

valoare_maxima = 0
while( i <= len(obiecte)-1 and greutate_maxima - obiecte[i][1] >= 0 ):

    sir1 += str(obiecte[i][1]) + "+"
    sir2 += str(obiecte[i][0]) + "+"
    valoare_maxima += obiecte[i][0]
    greutate_maxima -= obiecte[i][1]
    i += 1

valoare_maxima += (greutate_maxima/obiecte[i][1]) * obiecte[i][0]
sir1 +=  fractie(greutate_maxima,obiecte[i][1]) + "*" + str(obiecte[i][1]) + '\n\n'
sir2 +=  fractie(greutate_maxima,obiecte[i][1]) + "*" + str(obiecte[i][0]) + ' = ' + str(valoare_maxima)

g = open("rucsac.txt","w")
g.write(sir1 + sir2)
