import data
import ui
import logger

def buttun_click():
    var = ui.input_var()
    if var == '1':
        mathematical_expression = ui.get_data()
        number_list, oper_list = data.get_number(mathematical_expression)
    
        rezult = data.calk(oper_list, number_list)
        ui.rez(rezult)
        logger.data_recording(mathematical_expression, number_list, oper_list, rezult)
    
    if var == '2':
        x, y, oper = ui.complex_data()
        rezult = data.oper_x_y(x, y, oper)
        ui.rez(rezult)
        logger.data_recording_2(x, y, oper, rezult)
    