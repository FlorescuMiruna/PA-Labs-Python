f = open("inventar.txt")
d = {}
i =0
s = f.readlines()

for x in s:
    x = x[:-1]
    x = x.split()
    d1 = {x[i]: set(x[1:])}
    A = set(x[1: ])
    d.update(d1)

print(d)
B = set()

for x in d.values():
    A = A & x
    B = B | x
print(A)
print("Produsele care exista in toate magazinele: "  , end=" ")
for x in A:
    print(x, end=" ")
print('\n')
print("Toate produsele din toate magazinele: ",end=" ")
for x in B:
    print(x, end=" ")
print('\n')
for x,y in d.items():
    print (x, end=" ")
    for a in y-((B-y)|A):
        print(a,end=" ")
    print()

