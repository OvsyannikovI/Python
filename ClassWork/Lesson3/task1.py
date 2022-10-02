from random import choices


def name(a, b):
    name = []
    for i in range(a):
        y = choices(b, k=3)
        name.append("".join(y))
    return name


my_list = name(15, "abc")

print(my_list)


def find(word, arg):
    if word in arg and arg.count(word) > 1:
        ind = arg.index(word)
        print(arg.index(word, ind + 1))
    else:
        print(-1)
find("aba", my_list)