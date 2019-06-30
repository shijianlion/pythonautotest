from pageobject.elements import *
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
def login(self,username,password,expected):
    dr = self.driver
    dr.find_element(*username_loc).clear()
    dr.find_element(*username_loc).send_keys(username)
    dr.find_element(*password_loc).clear()
    dr.find_element(*password_loc).send_keys(password)
    dr.find_element(*btn_login_loc).cl

faefefefa44

grgr45454545
