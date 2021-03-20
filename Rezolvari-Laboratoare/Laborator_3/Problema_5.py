s = input("Propozitia este: ")
#s = s.split()
#print(s)
d1 = {x:s.count(x) for x in set(s.split())}
print(d1)

maxim = max(d1.values())
minim = min(d1.values())
d2 = {minim: set(x for x in d1.keys() if d1[x] == minim)}
d3 = {maxim: set(x for x in d1.keys() if d1[x] == maxim)}
print(d2)
for x in d2.values():
    cuv_rar = min(x)

for x in d2.values():
    cuv_des = max(x)

print("Cuvantul care apare cel mai des este : " + cuv_des)
print("Cuvantul care apare cel mai rar este : " + cuv_rar)
#print(d3)