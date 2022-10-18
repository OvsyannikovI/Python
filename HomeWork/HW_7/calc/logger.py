from datetime import datetime as dt
from time import time

def calc_logger(act,a,b,res):
    time_now = dt.now().strftime('%H:%M')
    with open('log_calc.csv', 'a') as file:
        file.write('{} : {} {} {} = {}\n'.format(time_now, a, act, b, res))

def calc_logger_mes(mes: str):
    time_now = dt.now().strftime('%H:%M')
    with open('log_calc.csv', 'a') as file:
        file.write('{} : {} \n'.format(time_now, mes))