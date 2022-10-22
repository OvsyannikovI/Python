# модуль добавления контакта
from codecs import utf_32_decode, utf_32_encode


def add_contact():
    data = input('Введите контакт (ФИО, номер):')
    with open('phone.csv', 'a') as file:
        for s in data.split(' '):
            file.write('{};'.format(s))
        file.write('\n')
    return print("Added")