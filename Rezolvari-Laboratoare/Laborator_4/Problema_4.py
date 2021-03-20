def prime():
    yield 2
    n = 3
    while True:
        i = 2
        ok = True
        while i*i <= n:
            if n % i == 0:
                ok = False
            i += 1

        if ok:
            yield n
        n += 2



n = int(input('n = '))

#a
print("Numerele prime mai mici sau egale cu",n,":")
generator = prime()
nr = next(generator)
while nr <= n:
    print(nr , end=' ')
    nr = next(generator)

#b
print('\n')
generator = prime()
print("Primele", n, "numere prime sunt:")
for i in range (n):
    nr = next(generator)
    print(nr,end =' ')