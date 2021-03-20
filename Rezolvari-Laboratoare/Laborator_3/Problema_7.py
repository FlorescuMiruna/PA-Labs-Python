d1 = {"Stefan": 3, "Ana":4, "Alin": 90,"Micu": 10}
d2 = {"Stefan": 10, "Ana": 76, "George": 10, "Alin": 10}
for nume_1,nr_1 in d1.items():
   for nume_2,nr_2 in d2.items():
       if(nume_1 == nume_2):
            d1[nume_1] = nr_1 + nr_2

#print(d1)
d2.update(d1)
print(d2)