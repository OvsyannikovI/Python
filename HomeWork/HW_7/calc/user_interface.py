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
    # print("Choose number")
    # while True:
    #     place_sign("O") if counter % 2 else place_sign("X")
    #     draw_board()

    #     if counter > 3:
    #         if check_win():
    #             print(f"{check_win()} - WIN{chr(127942)}{chr(127881)}!")
    #             break
    #     if counter == 8:
    #         print(f"Drawn game {chr(129318)}{chr(129309)}!")
    #         break
    #     counter += 1
