f = open("evenimente.txt")

def cmpOraInceput(t):
    return t[3]

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


f.close()

spectacole.sort(key=cmpOraInceput)
print(spectacole)
sali = []

for spectacol in spectacole:
    ok = 0
    for i in range(0,len(sali)):
        if spectacol[3] >= sali[i][len(sali[i])-1][4]:
            sali[i].append(spectacol)
           # print("case 1",sali)
            ok = 1 #inseamna ca am gasit o sala din cele deja folosite sa programam spectacolul
            break

    if ok == 0:
        sala_noua = []
        sala_noua.append(spectacol)
        sali.append(sala_noua)
       # print("case 2",sali)

g = open("sali.txt","w")
g.write(str(len(sali)) + " sali\n")
for x in sali:
    sir = ""
    for spectacol in x:
        sir += "(" + spectacol[0] + "-" + spectacol[1] + "  " + " " + spectacol[2] + ") , "
    sir = sir[:-2]
    sir += '\n'
    g.write(sir)
