import user_interface as ui

def get_value():
    return int(input('Enter number = '))

def select_item():
    print('Select item')
    num_menu = get_value()
    return num_menu

def control_main_menu(num: int):
    if str(num) in ui.menu_1:
        print("start")
    else:
        print("Error menu  --> ", num)

def add_contact():
    return print("")

def read_book():
    return print("")

def job_phone_book():
    control_main_menu(select_item())

