f = open("definitii.in")
lst = []
L = f.read()
sep ='":()=-,/.'
for x in L.split("+"):
    t = ()
    for y in sep:
        x = x.replace(y," ")
    x = x.split()
    cuv = x[0]
    #print(x)
    t =cuv , x.count(cuv) + x.count('~')-1
    lst.append(t)

print(lst)