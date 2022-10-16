prim = "101 / 2 - ( 12 + 8 ) * 3 / ( 13 * 8 ) "

actions = {
    "^": lambda x,y: str(float(x)**float(y)),
    "*": lambda x,y: str(float(x)*float(y)),
    "/": lambda x,y: str(float(x)/float(y)),
    "+": lambda x,y: str(float(x)+float(y)),
    "-": lambda x,y: str(float(x)-float(y)),
}

def InLine(line):
    my_list = []
    i = 0
    while i < len(line):
        if line[i] == "(":
            end_scob = line.index(")", i)
            my_list.append(line[i+1: end_scob])
            i = end_scob
        else:
            my_list.append(line[i])
        i +=1
    return my_list

print(InLine(prim.split()))

def DeLine(line):
    for i in range(len(line)):
        if isinstance(line[i], list):
            a, b, c = InLine(line[i])
            line[i] = actions[b](a, c)
    return line

print(DeLine(InLine(prim.split())))

def calc(line):
    prior = [i for i, j in enumerate(line) if j in '*/']
    while prior:
        t = prior[0]
        a, b, c = line[t - 1: t + 2]
        line.insert(t-1, actions[b](a, c))
        del line[t: t + 3]
        prior = [i for i, j in enumerate(line) if j in '*/']
    while len(line) > 1:
        a, b, c = line[: 3]
        del line[: 3]
        line.append(actions[b](a, c))
    return line

print(calc(DeLine(InLine(prim.split()))))
