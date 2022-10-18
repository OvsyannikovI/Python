import operations as op
import logger as log
import view

def button_click():
    act = view.get_value()
    if act == 6:
        log.calc_logger_mes("exit")
        exit()
    elif str(act) in op.dict_act:
        a = view.get_value()
        b = view.get_value()
        res = op.actions[op.dict_act.get(str(act))](a,b)
        log.calc_logger(op.dict_act.get(str(act)), a, b, res)
        print(res)
    else:
        print("Error")
        log.calc_logger_mes("Error")
    
