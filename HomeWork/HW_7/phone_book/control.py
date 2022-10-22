import user_interface as ui
import read_book as read
import add_contact as add

def get_value():
    return int(input('Enter number = '))

def select_item():
    print('Select item')
    num_menu = get_value()
    return num_menu

def control_main_menu(num: int):
    if str(num) in ui.menu_1:
        if num == 3:
            exit()
        elif num == 2:
            add.add_contact()
        elif num == 1:
            read.read_book()
    else:
        print("Error menu  --> ", num)



def job_phone_book():
    control_main_menu(select_item())

