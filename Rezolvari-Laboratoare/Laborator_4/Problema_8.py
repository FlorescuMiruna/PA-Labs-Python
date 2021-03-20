f = open("angajat.txt")
lst = [" "]
L = f.readlines()
print(L)
for i in range(len(L)):
    L[i] = list(L[i][:-1].split(" "))

    L[i][0] +=  lst[0]+L[i][1]
    L[i] = L[i][:1] + L[i][2:]
    #L[i]  L[i][0] + L[i][1]

print(L)
#a
nume = input("Numele angajatului: ")
for x in L:
    if x[0] == nume:
            print("Salariu:",x[2],'\n',"Varsta:",x[1],'\n')
