import test
import data

def input_var():
    var = input("Вас приветствует калькулятор!!!\nВведите какой пример вы будите решать: 1 - если обычный, 2 - если комплексный" '\n')
    return var

def get_data():
    return input('Введите пример = ')

def complex_data():
    x = complex(input("Введите первое комплексное число: "))
    y = complex(input("Введите второе комплексное число: "))
    oper = input("Введите математическую операцию: (+, -, *, /)")
       
    return x, y, oper

def rez(rezult):
    print(f'{rezult} результат')



# def get_value():
#     return test.get_ints()

# def get_oper():
#     return input('operator = ')

# def rez(rezult):
#     print(f'{rezult} результат')