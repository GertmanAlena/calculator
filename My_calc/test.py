

from asyncio.log import logger


def get_ints(char):
    '''
    проверка на ввод числа
    '''
    while True:
        try:
            return int(char)
        except ValueError:
            logger.input_ValueError(print('Ошибка. Ожидалось вещественное число.'))

def div(x, z, y):
    try:
        return x / y
    except ZeroDivisionError:
            print("нельзя делить на ноль")

