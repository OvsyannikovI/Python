# * 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов,
# заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

n1 = int(input("Введите первое число "))
n2 = int(input("Введите второе число "))
n3 = int(input("Введите количество элементов "))
print("Position one: ", n1)
print("Position two: ", n2)
print("Number of elements: ", n3)
my_list = []
rez = 1
for i in range(-n3, n3+1):
    my_list.append(i)
rez =my_list[n1-1] * my_list[n2-1]
print("-> ", my_list)
print("-> ", rez)