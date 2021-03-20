s = input("Numele este: ")
ok = 1
k = 0
for x in s:
    if not x.isalpha():
        if x == '-':
            k += 1
        else:
            if x != ' ':
                ok = 0
                break
if k > 1:
    ok = 0

if ok == 1:
    if k == 0:  #daca n-am cratima numele e de forma "Ana Avram"
        s = s.split()
        if len(s) != 2:
            ok = 0
        if len(s[0]) < 3 or len(s[1]) < 3:
            ok = 0
        if s[0][0].islower() or s[1][0].islower():
            ok = 0
    if k == 1: #daca am cratima numele e de forma "Ana Maria Avram"
        s = s.split()
        if len(s) != 2:
            ok = 0
        s[1] = s[1].split('-')
        if len(s[0]) < 3 or len(s[1][0]) < 3 or len(s[1][1]) < 3:
            ok = 0
        if s[0][0].islower() or s[1][0][0].islower() or s[1][1][0].islower():
            ok = 0
      #  print(s)



if ok == 1:
    print("Este un nume corect.")
else:
    print("Nu este un nume corect.")
