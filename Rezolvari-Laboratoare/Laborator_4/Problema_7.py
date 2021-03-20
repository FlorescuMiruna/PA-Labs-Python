f = open("cuvinte.txt",'r')
g = open("cuv_sortate.txt",'w')
L= f.read()
L= L.split()

L1 = sorted(L)
L1.reverse()


def cmpb(cuv):
    return len(cuv),cuv

L2 = sorted(L,key=cmpb)

def cmpc(cuv):
    return len(cuv)


L3 = sorted(L,key=cmpc)


g.write(str(L)+'\n')
g.write(str(L1)+'\n')
g.write(str(L2)+'\n')
g.write(str(L3)+'\n')

