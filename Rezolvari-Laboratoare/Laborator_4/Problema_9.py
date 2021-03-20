#a
def citire():
    n = int(input("Numar de numere: "))
    lst = []
    for i in range(n):
        x = int(input("Numarul este: "))
        lst.append(x)
    return  n,lst;


nr,lst=citire()

print(lst)

#b

def functie(i,j, x,lst):
    for l in range(i,j+1):
        if lst[l]>x:
            return l;
            break
    else:
        return  -1;

nr = functie(0,3,6,lst)
print(nr)

k=0
for x in lst:
    k+=1
    print(functie(k,len(lst),x,lst))
