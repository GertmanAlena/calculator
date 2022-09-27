import test

def get_number(mathematical_expression):
    number = []
    alem = []
    temp_num = '' # тут склеиваем цифры
    mathematical_expression += '='
    for char in mathematical_expression:
        if char.isdigit():
            temp_num += char
        else:
            number.append(temp_num)
            alem.append(char)
            temp_num = ''
       
    return number, alem[:-1]

def pop_insert_list(number_list, index_alem, num, oper_list):
    number_list.pop(index_alem)
    number_list.pop(index_alem)
    number_list.insert(index_alem, num)
    oper_list.pop(index_alem)

def calk(oper_list, number_list):

    operators_list = ['/', '*', '-', '+']
    priority_list = [1, 1, 2, 2]
    unite_list = list(zip(priority_list, operators_list))

    operators = {
    '*': lambda x, y: int(x)*int(y),
    '/': lambda x, y: int(x)/int(y),
    '+': lambda x, y: int(x)+int(y),
    '-': lambda x, y: int(x)-int(y)
    }
    for i in unite_list:                
        if i[0] == 1:           # i в (1, '/'), (1, '*')
            for j in oper_list: # ['-', '+', '*', '=']
                if j == i[1]:
                    index_alem = oper_list.index(j)
                    if j in ' /':
                        while j in oper_list:
                            if int(number_list[index_alem+1]) == 0:
                                print("нельзя делить на ноль") 
                                break
                            else:    
                                num = operators[j](number_list[index_alem], number_list[index_alem+1])
                                pop_insert_list(number_list, index_alem, num, oper_list)
                             

                    if j in '*':
                        while j in oper_list:
                            num = operators[j](number_list[index_alem], number_list[index_alem+1])
                            pop_insert_list(number_list, index_alem, num, oper_list)
    for i in unite_list:    
        if i[0] == 2:           
            for j in oper_list:
                
                if j == i[1]:
                    index_alem = oper_list.index(j)
                   
                    if j in '-':
                        while j in oper_list:
                            num = operators[j](number_list[index_alem], number_list[index_alem+1])
                            pop_insert_list(number_list, index_alem, num, oper_list)
                    if j in '+':
                        while j in oper_list:
                            num = operators[j](number_list[index_alem], number_list[index_alem+1])
                            pop_insert_list(number_list, index_alem, num, oper_list)
    return number_list

def oper_x_y(x, y, oper):
    if oper == '+':
        return x + y
    elif oper == '-':
        return x - y  
    elif oper == '*':
        return x * y
    elif oper == '/':
        test.div(x, y)
        return x / y 

# def addition(x, y):
#     return x + y
# def difference(x, y):
#     return x - y
# def multiplication(x, y):
#     return x * y
# def division(x, y):
#     return x / y