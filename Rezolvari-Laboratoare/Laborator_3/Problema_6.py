f = open("textlorem.in", 'r')
text = f.read()

d = {x: text.count(x) for x in set(text)}
print(d)