s = input("Sirul este: ")
s = [int(x) for x in s.split()]
s.sort()
s.reverse()
maxim_1 = s[0]
i = 0
ok = 0
for x in s:
    if x != maxim_1:
        maxim_2 = x
        ok = 1
        break

if ok == 1:
    print("Cele mai mari doua valori distincte din sir sunt:",maxim_2,"si",maxim_1)
else:
    print("Nu exista doua valori distincte in sir. Maximul este:",maxim_1)