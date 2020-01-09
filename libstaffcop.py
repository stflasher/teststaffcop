from values import *


def login(arg,_login,_pass):
    arg.find_element_by_id(el_login).clear()
    arg.find_element_by_id(el_login).send_keys(_login)
    arg.find_element_by_id(el_pass).clear()
    arg.find_element_by_id(el_pass).send_keys(_pass)
    arg.find_element_by_xpath(btn_input).click()

def open_menu_admin(driver, var_item):
    driver.find_element_by_link_text(MENU_ADMIN).click()
    driver.find_element_by_link_text(var_item).click()