from secrets import randbelow


max = 0
for i in range(5):
    a = int(input())
    if a > max:
        max = a
print(max)