import datetime
from better_log import coloredtext
from colorama import Fore, Back


def new_log(logdebug, typee='info'): # NOQA
    hour = datetime.datetime.now().hour
    if len(str(hour)) == 1:
        hour = "0" + str(hour)

    minute = datetime.datetime.now().minute
    if len(str(minute)) == 1:
        minute = "0" + str(minute)

    second = datetime.datetime.now().second
    if len(str(second)) == 1:
        second = "0" + str(second)

    if typee == 'warn':
        print(coloredtext.color(f'[{hour}:{minute}:{second}] [{typee}]: {logdebug}', Fore.LIGHTYELLOW_EX))
    elif typee == 'error':
        print(coloredtext.color(f'[{hour}:{minute}:{second}] [{typee}]: {logdebug}', Fore.LIGHTRED_EX))
    elif typee == 'fatal':
        print(coloredtext.color(f'[{hour}:{minute}:{second}] [{typee}]: {logdebug}', Fore.RED, Back.BLACK))
    else:
        print(f'[{hour}:{minute}:{second}] [{typee}]: {logdebug}')
    # return f'[{hour}:{minute}:{second}] [{typee}]: {logdebug}' # NOQA

