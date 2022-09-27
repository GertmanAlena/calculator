from datetime import datetime as dt
import logging
from time import time

# logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s' )
# logging.debug( 'Это сообщение журнала.' )


# logging.basicConfig(level=logging.INFO, filename="result.txt",filemode="a")
# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")

def data_recording(mathematical_expression, number_list, oper_list, rezult):

    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write(time + '\n')
        file.write('\n' + f'{mathematical_expression} = пример' + '\n')
        file.write(f'"{number_list}" = список чисел' + '\n')
        file.write(f'{oper_list} = список операций' + '\n')
        file.write(f'результат вычисления = {rezult}')

def data_recording_2(x, y, oper, rezult):

    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write(time + '\n')
        file.write('\n' + f'{x} = x' + '\n')
        file.write(f'{y} = y' + '\n')
        file.write(f'{oper} = действие' + '\n')
        file.write(f'результат вычисления = {rezult}')

def input_ValueError(mass):

    time = dt.now().strftime('%d-%b-%y %H:%M:%S')
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write(time + '\n')
        file.write('\n' + f'{mass} = ошибка' + '\n')
        
