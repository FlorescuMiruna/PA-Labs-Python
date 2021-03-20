from math import pi

def lungime_arie_cerc(r):
    return 2 * pi * r, pi * (r**2)

raza = float(input("Raza este: "))

lungime, arie = lungime_arie_cerc(raza)

print("Lungimea este:",lungime)
print("Aria este:",arie)
