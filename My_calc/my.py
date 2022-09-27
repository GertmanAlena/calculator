data = input('Введите пример - > ')   
 
operators_list = ['/', '*', '-', '+']
priority_list = [1, 1, 2, 2]
'''
[(1, '/'), (1, '*'), (2, '+'), (2, '-')]
'''
unite_list = list(zip(priority_list, operators_list))
print(unite_list)

def get_number(data):
    number = []
    alem = []
    temp_num = '' # тут склеиваем цифры
    data += '='
    for char in data:
        if char.isdigit():
            temp_num += char
        else:
            number.append(temp_num)
            alem.append(char)
            temp_num = ''
    return number, alem[:-1]

                                          #  [(1, '/'), (1, '*'), (2, '+'), (2, '-')]  unite_list
number_list, oper_list = get_number(data)  # ['22', '2', '5', '2']   ['-', '+', '*', '=']
print(number_list, oper_list)

def pop_insert_list(number_list, index_alem, num, oper_list):
    number_list.pop(index_alem)
    number_list.pop(index_alem)
    number_list.insert(index_alem, num)
    oper_list.pop(index_alem)
   
def calk(unite_list, oper_list, number_list):
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
                        
rezult = calk(unite_list, oper_list, number_list)
print(rezult)