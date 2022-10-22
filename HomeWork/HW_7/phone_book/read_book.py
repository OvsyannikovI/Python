# модуль чтения книги


def read_book():
    with open('phone.csv', 'r') as file:
        lines = file.readlines()
        # итерация по строкам
        for line in lines:
            print(line.replace(';', ' '))
    return print("Read")
