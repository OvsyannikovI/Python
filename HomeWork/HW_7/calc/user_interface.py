import logger as log
import operations as op
import control as cn

def main_menu():
    print('-' * 20)
    print("Mini Calc")
    print('-' * 20)
    j = 1
    for i in op.actions.keys():
        print(f"{j} --- '{i}'")
        j += 1
    print("6 --- exit")
    print('-' * 20)
    cn.button_click()

