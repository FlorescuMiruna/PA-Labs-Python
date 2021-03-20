f = open("rime.in")
g = open("rime.out", "w")
text = f.read()
f.close()

sep = ",.!?-"
for x in sep:
    text = text.replace(x, ' ')

d = { x[-3:] for x in text.split()}

for x in d:
    lst = []
    for y in text.split():
        if (y[-3:] == x):
            lst.append(y)
    g.write(' ,'.join(lst) + "\n")

print(d)