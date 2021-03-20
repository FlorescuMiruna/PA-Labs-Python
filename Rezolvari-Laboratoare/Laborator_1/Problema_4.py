n = int(input("n = "))
anterior = float(input())
maxim = 0
diferenta = 0
ziua_1 = 0
ziua_2 = 0
for i in range(1,n):
    current = float(input())
    diferenta = current - anterior
    anterior = current
    if diferenta >= maxim:
        maxim = diferenta
        ziua_1 = i
        ziua_2 = i+1

maxim *= 100
maxim = int(maxim)
maxim /= 100
print("Cea mai mare crestere a fost de:",maxim,"RON intre zilele ", ziua_1,"si",ziua_2)
