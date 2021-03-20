f = open("bani.txt")
monede = f.readline()
monede = [int(x) for x in monede.split()]

moede = monede.reverse()

suma = int(f.readline())
sir = str(suma) + " = "
indice = 0
plata = []
while suma != 0:

    moneda = monede[indice]
    nr = 0
    while suma - monede[indice] >= 0:
        suma -= monede[indice]
        nr += 1

    if nr != 0:
        plata.append((moneda,nr))

    indice += 1


print(plata)



for x in plata:
    sir += str(x[0]) + "*" + str(x[1]) + " + "

g = open("plata.txt","w")
g.write(sir[:-2])


