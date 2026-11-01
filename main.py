import time
from datetime import datetime as dt

def first_decor(func):
    def wrapper(*args, **kwargs):
        print(f'Декоратор принимает на вход функцию {func.__name__}, она начинает работу.')
        start = dt.now()
        func(*args, **kwargs)
        end = dt.now()
        print(f'Время работы функции {func.__name__}: {end-start}')
        print(f'{func.__name__} завершила работу.')
    return wrapper

@first_decor
def delay(sec:float):
    time.sleep(sec)


@first_decor
def summ(*args):
    res = 0
    if not args:
        return res
    else:
        for a in args:
            if isinstance(a, (int, float)):
                res += a
        return res


delay(2)
print(summ())