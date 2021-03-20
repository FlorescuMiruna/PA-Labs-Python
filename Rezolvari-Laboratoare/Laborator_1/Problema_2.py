L1 = int(input("L1 = "))
L2 = int(input("L2 = "))
a = L1
b = L2
while(b):   #algoritmul lui Euclid pentru cmmdc
    c = a%b
    a = b
    b = c

nr_placi = L1/a * L2/a
print("Mesterul are nevoie de " , nr_placi, "de placi de gresie, cu latura de",a,"cm")

