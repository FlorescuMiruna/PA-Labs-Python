from string import digits, ascii_lowercase, ascii_uppercase
from random import choices

f = open("date.in", 'r')
g = open("date.out", 'w')

L = f.readlines()
f.close()
parola = ''
for s in L:
    [nume,prenume] = s[:-1].split(" ")
    email = (prenume + '.' + nume).lower() + "@myfmi.unibuc.ro"

    litera_mare = choices(ascii_uppercase)
    litere_mici = choices(ascii_lowercase, k = 3)
    numere = choices(digits, k = 4)

    parola = ''.join(litera_mare + litere_mici + numere)

    g.write(email + ',' + parola + '\n')

g.close()