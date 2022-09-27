

def get_ints():
    '''
    проверка на ввод числа
    '''
    while True:
        try:
            num = int(input('value = '))
            return num
        except ValueError:
            print('Ошибка. Ожидалось вещественное число.')

def div(x, z, y):
    try:
        return x / y
    except ZeroDivisionError:
            print("нельзя делить на ноль")
