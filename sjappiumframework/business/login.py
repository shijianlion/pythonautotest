from pageobject.elements import *
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
def login(self,username,password,expected):
    dr = self.driver
    dr.find_element(*username_loc).clear()
    dr.find_element(*username_loc).send_keys(username)
    dr.find_element(*password_loc).clear()
    dr.find_element(*password_loc).send_keys(password)
    dr.find_element(*btn_login_loc).click()
    WebDriverWait(dr, 20, 0.5).until(EC.presence_of_element_located(msg_login_success_loc)) 
    actual = dr.find_element(*msg_login_success_loc).text
    self.assertEqual(expected, actual,"使用正常的帐号登录，但是没有登录成功，测试用例FAIL")
