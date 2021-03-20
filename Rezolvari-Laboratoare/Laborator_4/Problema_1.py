def ipotenuza(a,b):
    c = a**2 + b**2
    c = c**0.5
    return c

print(ipotenuza(6,8))

b = int(input("b = "))
g = open("triplete_pitagoreice.txt","w")

for a in range(1,b+1):
    c = ipotenuza(a,b)
    if c.is_integer():
        g.write('a  = '+ str(a)+ ',b = '+ str(b)+',c ='+ str(int(c))+"\n")


g.close()