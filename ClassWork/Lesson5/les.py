path = "file.txt"
f = open(path, 'r')
data = f.read() + ' '
f.close()

num = []

while data != '':
    space_pos = data.index(' ')
    num.append(int(data[:space_pos]))
    data = data[space_pos+1:]

out = []

for e in num:
    if not e % 2:
        out.append((e,e**2))

print(out)
