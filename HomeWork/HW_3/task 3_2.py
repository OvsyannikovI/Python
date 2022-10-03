# 2. Напишите программу, которая 
# найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]
import random

count = int(input("Введите количество чисел списка: "))

def createList(num):
    my_list = []
    for i in range(num):
        my_list.append(round(random.random()*10))
    return my_list

arr = createList(count)
print(arr)

def PrList(my_array):
    rez = []
    lght = len(my_array)
    for i in range(0,int(lght/2)):
        rez.append(int(my_array[i]) * int(my_array[-(i+1)]))
    if lght%2 == 0 :
       return rez
    else:
        rez.append(my_array[int(lght/2)])
        return rez

print(PrList(arr))
