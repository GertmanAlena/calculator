import data
import ui
import logger

def buttun_click():
    value_x = ui.get_value()
    value_y = ui.get_value()
    value_z = ui.get_oper()
    data.num(value_x, value_y, value_z)
    rezult = data.operator()
    ui.rez(rezult)
    logger.data_recording(value_x, value_y, value_z, rezult)