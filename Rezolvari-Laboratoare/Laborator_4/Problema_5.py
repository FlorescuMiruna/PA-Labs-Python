def negative_pozitive(lst):
    lst_negative = [x for x in lst if x < 0]
    lst_pozitive = [x for x in lst if x > 0]
    return  lst_negative,lst_pozitive

lst = [1,232, 21,-181,0,-1,-2,-3,100]

a,b = negative_pozitive(lst)

nume = input("Numele fisierului: ")
g = open(nume+'.txt', 'w')
for x in a:
    g.write(str(x)+' ')

g.write('\n')

for x in b:
    g.write(str(x)+' ')

