# 3. Задайте последовательность чисел.
#  Напишите программу, которая выведет 
#  список неповторяющихся элементов исходной 
#  последовательности в том же порядке.

# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]
import random

count = int(input("Введите количество чисел списка: "))

def createList(num):
    my_list = []
    for i in range(num):
        my_list.append(round(random.random()*10))
    return my_list

arr = createList(count)
print(arr)

def DelClone(my_list): 
    new_list = []
    
    for i in my_list:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list

print(DelClone(arr))