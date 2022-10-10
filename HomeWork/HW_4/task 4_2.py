# 2. Задайте натуральное число N.
# Напишите программу, которая составит 
# список простых множителей числа N.

# in
# 54
# out
# [2, 3, 3, 3]
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
# in
# 650
# out
# [2, 5, 5, 13]

numberInput = int(input("Введите простое число: "))

def GetListSimpleNum(num):
    my_list = []
    num1 = 2
    while num1 * num1 <= num:
        if num % num1 == 0:
            my_list.append(num1)
            num //= num1
        else:
            num1 += 1
    if num > 1:
        my_list.append(num)
    return my_list

print(GetListSimpleNum(numberInput))
