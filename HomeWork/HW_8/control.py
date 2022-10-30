import user_interface as ui
import read_emply as read
import add_emply as add

def get_value():
    return int(input('Enter number = '))

def select_item():
    print('Select item')
    num_menu = get_value()
    return num_menu

def control_main_menu(num: int):
    if str(num) in ui.menu_1:
        if num == 0:
            exit()
        elif num == 1:
            read.read_shtat()
        elif num == 2:
            read.read_dol()
        elif num == 3:
            read.read_emply()
        elif num == 4:
            add.add_emply()
        elif num == 5:
            print('')
        elif num == 6:
            print('')
        elif num == 7:
            read.read_book()
    else:
        print("Error menu  --> ", num)
        control_main_menu(select_item())



def start_program():
    control_main_menu(select_item())

def search(data):
    flag = 1
    name = input('Введите фамилию > ')
    for line in data:
        if name in line:
            flag = 0
            print(f"\033[32m {line} \033[39m")
    if flag: print('no name given')
    search(data)