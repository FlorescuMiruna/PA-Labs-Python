a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
delta = b**2 - 4*a*c
if delta < 0:
    print("Ecuatia nu are soltutii reale")
else:
    x1 = (-b + delta**0.5)/(2*a)
    x2 = (-b - delta**0.5)/(2*a)
    if x1 == x2:
        print("Ecuatia are o singura solutie reala:", x1)
    else:
        print("Ecuatia are doua solutii reale:",x1,"si",x2)
