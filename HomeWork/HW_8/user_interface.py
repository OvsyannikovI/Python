import control as cn

menu_1 = {
    "1": "Показать штат",
    "2": "Список должностей",  
    "3": "Список сотрудников", 
    "4": "Добавить сотрудника", 
    "5": "Удалить сотрудника", 
    "0": "Exit",  
}

def main_menu():
    print('-' * 20)
    print("Штат поликлиники")
    print('-' * 20)
    for item in menu_1:
        print(f"{item} --> {menu_1[item]}")
    print('-' * 20)
    cn.start_program()