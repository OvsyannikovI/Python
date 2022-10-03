# 3. Напишите программу, которая будет 
# преобразовывать десятичное число в двоичное.
# Без использования встроенной 
# функции преобразования, без строк.
# in
# 88
# out
# 1011000
# in
# 11
# out
# 1011

numberInput = int(input("Введите чисело: "))

def ToDoubleNumber(num):
    pow=1
    dec=0
    while num>0:
        dec=dec+num%2*pow
        pow*=10
        num=num//2
    return dec

print(ToDoubleNumber(numberInput))