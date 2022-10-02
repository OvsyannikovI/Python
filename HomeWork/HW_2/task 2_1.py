# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

num = float(input())
print(num," -> ")
count = len(str(num))
num = int(num * 10 ** count)
rez = 0
while num // 10 > 0:
    rez = rez + num % 10
    num = num // 10
else:
    rez = rez + num % 10
print(rez)