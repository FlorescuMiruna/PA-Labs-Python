def citire(v):
    n = int(input("n = "))
    for i in range(n):
        x = int(input("Element: "))
        v.append(x)


def afisare(v):
    for x in v:
        print(x,end=' ')

def valpoz(v):
    lst = []
    lst = [x for x in v if x>=0]
    return lst

def semn(v):
    for i in range(len(v)):
        v[i] = v[i]*(-1)




v = []
citire(v)
lst = valpoz(v)
afisare(lst)
print()
semn(v)
lst = valpoz(v)
for x in lst:
    if x == 0:
        lst.remove(x)
semn(lst)
afisare(lst)
