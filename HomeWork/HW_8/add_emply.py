# модуль добавления контакта
import control as cn
import user_interface as ui
from codecs import utf_32_decode, utf_32_encode
import read_emply as read


def add_emply():
    print('Добавление сотрудника')
    data = input('Фамилия: ')
    data += ' ' + input('Имя: ')
    data += ' ' + input('Отчество: ')
    data += ' ' + input('Дата рождения: ')
    print('#' * 20)
    print("Список должностей")    
    print('-' * 20)
    with open('C:/Python/HomeWork/HW_8/dol.csv', 'r', encoding = 'utf-8') as file1:
        lines = file1.readlines()
        i = 1
        for line in lines:
            print(f"{i} -- {line}")
            i += 1   
    print('#' * 20)
    data += ' ' + str(int(input('Должность из списка: ')) - 1)  
    with open('C:/Python/HomeWork/HW_8/emply.csv', 'a', encoding = 'utf-8') as file:
        for s in data.split(' '):
            file.write('{};'.format(s))
        file.write('\n')
    return ui.main_menu()