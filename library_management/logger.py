import config
import datetime


def debug_print(message, calling_method_name='default'):
    if config.RUN_MODE == 'debug':
        print(f"[DEBUG]\t[{calling_method_name}]\t{datetime.datetime.now()}\t{message}")
