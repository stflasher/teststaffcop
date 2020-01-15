# testsstaffcop
tests for staffcop on selenium (language python)

Запускать тест 

maintestselenium.py

Переменные:

values.py

Библиотека :

libstaffcop.py

если данных за сутки нет то под строкой :

driver.find_element_by_xpath(BTN_HOME).click()

добавить команды, которые выберут из календаря 14 января:
driver.find_element_by_xpath("//div[@id='reportrange']/span").click()

driver.find_element_by_xpath("//tr[3]/td[4]").click()

driver.find_element_by_xpath("//tr[3]/td[4]").click()
