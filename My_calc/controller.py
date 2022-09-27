import data
import ui
import logger

def buttun_click():
    mathematical_expression = ui.get_data()
    number_list, oper_list = data.get_number(mathematical_expression)
    
    rezult = data.calk(oper_list, number_list)
    ui.rez(rezult)
    logger.data_recording(mathematical_expression, number_list, oper_list, rezult)