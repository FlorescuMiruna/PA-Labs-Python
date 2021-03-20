f = open("cheltuieli.txt", 'r')
sir = f.read()
f.close()
suma = 0
sir = sir.split()
for x in sir:
    if x.isdecimal():
        print(int(x))
        suma = suma + int(x)
    else:
        y = x.split('.')
        if len(y) == 2:
            if y[0].isdecimal() and y[1].isdecimal():
                print(float(x))
                suma = suma + float(x)

print("Suma totala cheltuita de Ana este:",suma,"RON")