# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.

# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]
import random

count = int(input("In : "))

def createList(num):
    my_list = []
    for i in range(count):
        my_list.append(round(random.random()*10))
    return my_list

arr = createList(count)

def rezList(list):
    new_list = []
    for i in range(1, len(list)):
        if list[i] > list[i - 1]:
            new_list.append(list[i])
    return new_list

print(arr)
print(rezList(arr))