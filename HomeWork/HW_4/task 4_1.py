# 1. Вычислить число c заданной точностью d

# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988

from decimal import Decimal

numberInput = (input("Enter a real number: "))
reqAcc = (input("Enter the required accuracy '0.0001': "))

def ToAcc(numberInput, reqAcc):
    num = Decimal
    return num(numberInput).quantize(num(reqAcc))

print(ToAcc(numberInput, reqAcc))