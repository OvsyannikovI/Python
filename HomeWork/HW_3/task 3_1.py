# 1. Задайте список, состоящий из произвольных
#  чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму
#  элементов списка, стоящих на нечётных 
# позициях(не индексах).

# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22
import random

count = int(input("Введите количество чисел списка: "))

def createList(num):
    my_list = []
    for i in range(count):
        my_list.append(round(random.random()*10))
    return my_list

arr = createList(count)

print(arr)
sum = 0
for i in range(0, len(arr)):
    if (i+1)%2 == 0:
        sum += int(arr[i])
print(sum)
