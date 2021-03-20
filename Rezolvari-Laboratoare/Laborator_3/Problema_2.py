f = open("test.in", 'r')
g = open("test.out", 'w')
nota = 1
raspuns = ''
for i in range(9):
    x = f.readline()
    x = x[:-1]
    sir = x
    x = x.split('=')
    a,b = x[0].split('*')
    a = int(a)
    b = int(b)
    c = x[1].strip()
    c = int(c)
    print(type(c),c)
    d = a*b
    if c == d:
        raspuns = sir + ' ' + "Corect"
        nota += 1
    else:
        raspuns = sir + ' ' + "Gresit" + ' ' + str(d)
    g.write(raspuns + '\n')
print(nota)
g.write(str(nota))
f.close()
g.close()