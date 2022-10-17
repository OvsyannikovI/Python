import operations as op
import view

def button_click():
    act = view.get_value()
    if act == 6:
        exit()
    elif act in op.dict_act.keys():
        res = op.actions[op.dict_act[act]](view.get_value(),view.get_value())
    else:
        print("Error")
    # view.view_data(res)