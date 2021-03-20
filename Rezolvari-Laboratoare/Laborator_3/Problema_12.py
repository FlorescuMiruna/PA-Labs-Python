lst = []
s = input()
a = ()
s = s.split(" ",1)
k = 0
a = s[0], s[1], k
k += 1
lst.append(a)
while s != '-1':
    s = input()
    if(s != '-1'):
        a = ()
        s = s.split(" ",1)
        a = s[0], s[1], k
        k += 1
        lst.append(a)

lst = [('100', 'ana avram ', 0), ('100', 'ana maria', 1), ('300', 'florescu miruna', 2), ('400', 'luca stefan', 3)]
multime = set()
for x in lst:
    multime.add(x[0])

print(multime)

d = {}

for x in multime:
    di = {}
    lista = []
    for y in lst:
        if x == y[0]:
            lista.append(y[1:])
            print(y[1:])
    di = {x:lista}
    d.update(di)

print(d)
d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

print(d)
