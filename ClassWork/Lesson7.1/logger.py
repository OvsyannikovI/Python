from datetime import datetime as dt
from time import time

def temperature_logger(data):
    time_now = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};temperature;{}\n'.format(time_now, data))

def preassure_logger(data):
    time_now = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};preassure;{}\n'.format(time_now, data))

def wind_speed_logger(data):
    time_now = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};wind_speed;{}\n'.format(time_now, data))