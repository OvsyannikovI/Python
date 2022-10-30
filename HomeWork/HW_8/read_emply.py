# модуль чтения книги
import control as cn
import user_interface as ui
from codecs import utf_32_decode, utf_32_encode


def read_emply():    
    print('#' * 20)
    print("Список сотрудников")
    print('-' * 20)
    with open('C:/Python/HomeWork/HW_8/emply.csv', 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
        emp = []
        for line in lines:
            emp.append("".join(line.replace(";", " ")))
            print(emp)
            # print(f"{i} -- {line.replace(';', ' ')}")
        print (" ".join(emp))
    print('#' * 20)
    return ui.main_menu()

def read_dol():
    print('#' * 20)
    print("Список должностей")    
    print('-' * 20)
    with open('C:/Python/HomeWork/HW_8/dol.csv', 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
        i = 1
        for line in lines:
            print(f"{i} -- {line}")
            i += 1   
    print('#' * 20)
    return ui.main_menu()

def read_shtat():
    print('#' * 20)
    print("Штат сотрудников")    
    print('-' * 20)
    shtat = []
    with open('C:/Python/HomeWork/HW_8/dol.csv', 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
        for line in lines:
            shtat.append(line)
    print('#' * 20)
    return ui.main_menu()
