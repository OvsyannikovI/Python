import control as cn

menu_1 = {
    "1": "Read book",
    "2": "Add contact",  
    "3": "Exit",  
}

def main_menu():
    print('-' * 20)
    print("Phone book")
    print('-' * 20)
    for item in menu_1:
        print(f"{item} --> {menu_1[item]}")
    print('-' * 20)
    cn.job_phone_book()
