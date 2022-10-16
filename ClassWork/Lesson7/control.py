import model_mult as mm
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    mm.init(value_a, value_b)
    res = mm.do_it()
    view.view_data(res)