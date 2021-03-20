f = open("cuburi.in",'r')

nr = int(f.readline())

def cmpInaltime(t):
    return -t[0]

cuburi = []
for linie in f.readlines():
    linie = linie.split()
    cuburi.append((int(linie[0]),linie[1]))

f.close()
cuburi.sort(key=cmpInaltime)
print(cuburi)

g = open("cuburi.out","w")

culoare = ""
inaltime = 0
for cub in cuburi:
    if cub[1] != culoare:
        g.write(str(cub[0]) + " " + cub[1] + "\n")
        culoare = cub[1]
        inaltime += cub[0]

g.write("Inaltimea totala este: "+  str(inaltime))
