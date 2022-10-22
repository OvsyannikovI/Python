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
        c = view.isNumeric(a)
        print(c)
        d = view.isNumeric(b)
        print(d)
        if c == False or d == False:
            res = op.actions_float[op.dict_act.get(str(act))](float(a),float(b))
            log.calc_logger(op.dict_act.get(str(act)), float(a), float(b), float(res))
            return print(res)
        else:
            res = op.actions_complex[op.dict_act.get(str(act))](complex(a),complex(b))
            log.calc_logger(op.dict_act.get(str(act)), complex(a), complex(b), complex(res))
            return print(res)
    else:
        print("Error")
        log.calc_logger_mes("Error")
    
