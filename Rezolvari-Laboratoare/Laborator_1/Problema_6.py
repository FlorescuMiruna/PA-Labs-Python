n = int(input("n = "))
ap = {}
ap = {x: 0 for x in range(10)}
nr_cel_mai_mic = 0
nr_cel_mai_mare = 0

while n:
    u = n%10
    ap[u] +=1
    n //=10

x = ap[1]
while (x):
    nr_cel_mai_mic = nr_cel_mai_mic * 10 + 1
    x = x - 1

x = ap[0]
while (x):
    nr_cel_mai_mic = nr_cel_mai_mic * 10 + 0
    x = x - 1

for i in range(2,10):
    x = ap[i]
    while x:
        nr_cel_mai_mic = nr_cel_mai_mic*10 + i
        x = x-1



for i in range(9,-1,-1):
    x = ap[i]
    while x:
        nr_cel_mai_mare = nr_cel_mai_mare*10 + i
        x = x-1

print("Numarul cel mai mic care se poate forma este", nr_cel_mai_mic)
print("Numarul cel mai mare care se poate forma este",nr_cel_mai_mare)