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
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(time + '\n')
        file.write('\n' + f'{mathematical_expression} = пример' + '\n')
        file.write(f'"{number_list}" = список чисел' + '\n')
        file.write(f'{oper_list} = список операций' + '\n')
        file.write(f'результат вычисления = {rezult}')


        # file.write('{}; value_x:{}; value_y:{}; value_z:{}; rezult:{}'.format(time, value_x, value_y, value_z, rezult))
# with open('students.txt', 'w', encoding='utf-8') as data:  # пока работа в txt через data
# 	for i in Students:
# 		data.write(i + '\n') #записали в txt файл через data.write наш словарь
# def number_y(data):
#     '''
    
#     '''
#     time = dt.now.strftime('%d-%b-%y %H:%M:%S')
#     with open('result.txt', 'a', encoding='utf-8') as file:
#         file.write('{}; number_y:{}'.format(time, data))

# def number_selectoperation(data):
#     '''
    
#     '''
#     time = dt.now.strftime('%d-%b-%y %H:%M:%S')
#     with open('result.txt', 'a', encoding='utf-8') as file:
#         file.write('{}; number_selectoperation:{}'.format(time, data))
