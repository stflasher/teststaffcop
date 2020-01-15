# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

from libstaffcop import *
from values import *

class MainTestSelenium(unittest.TestCase):
    
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        options = Options()
        options.add_argument(LANGUAGE)
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = URL
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get(self.base_url)
        login(driver,val_login,val_pass)
        driver.implicitly_wait(30)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, MENU_ADMIN))).click()
        element=driver.find_element_by_link_text(CONTROL_PANEL)
        hov = ActionChains(driver).move_to_element(element)
        hov.perform()
        hov.reset_actions()
        dropdown_menu = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, P_SETTINGS)))
        dropdown_menu.click()
        x = driver.find_element_by_xpath(TEXT_DIMENSTION).text
        if x!="Accounts":
            driver.find_element_by_link_text(D_DIMENSION).click()        
            driver.find_element_by_id(VALUE_D_DIMENSION).click()
            Select(driver.find_element_by_id(VALUE_D_DIMENSION)).select_by_visible_text(ACCOUNTS_D_DIMENSION)
            driver.find_element_by_xpath(BUTTON_D_DIMENSION).click()
            driver.find_element_by_name(BTN_SAVE_DIMENSION).click()
        driver.find_element_by_xpath(BTN_HOME).click()
        driver.find_element_by_xpath("//div[@id='reportrange']/span").click()
        driver.find_element_by_xpath("//tr[3]/td[4]").click()
        driver.find_element_by_xpath("//tr[3]/td[4]").click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, MENU_TIME_TRACKING))).click()
        #driver.implicitly_wait(30)
        driver.find_element_by_link_text(COMBINED_REPORT).click()
        #driver.implicitly_wait(30)
        page=driver.find_element_by_xpath(NAME_PAGE)
        if "Account" in page.text:
            print("Functional is work")
        else:
            print("The function is broken")
        driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
