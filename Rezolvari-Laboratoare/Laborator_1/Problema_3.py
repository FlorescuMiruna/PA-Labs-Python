x = int(input("x = "))
n = int(input("n = "))
p = int(input("p = "))
m = int(input("m = "))
lungime = 0
while m!=0:
    lungime = lungime + n*x
    x = x-p/100*x
    m = m-n
print("Lungimea parcursa de greiere este de ",int(lungime),"de cm")