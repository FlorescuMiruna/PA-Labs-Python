f = open("spectacole.in")

def cmpOraFinal(t):
    return t[4]

spectacole = []
for linie in f:
    linie = linie.split(" ",1)
    aux = linie[0].split("-")
    tuplu = aux[0],aux[1]
    tuplu += (linie[1][:-1],)

    ore,minute = aux[0].split(":")
    minute = int(ore)*60 + int(minute)
    tuplu += (minute,)

    ore,minute = aux[1].split(":")
    minute = int(ore)*60 + int(minute)
    tuplu += (minute,)

    spectacole.append(tuplu)
    print(linie)

f.close()
print(spectacole)
print(spectacole[1][3])
spectacole.sort(key = cmpOraFinal)
print(spectacole)

g = open("spectacole.out","w")


ultima_ora = 0

for x in spectacole:
    if x[3] > ultima_ora:
        ultima_ora = x[4]
        sir = " "
        sir = x[2] + " " + x[0] + " " + x[1] + "\n"
        g.write(sir)



