# __Author:"Levente Liu"

from selenium import webdriver
import time
import unittest
from test_case.util.read_method import ReadElement

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.read_element = ReadElement(self.driver)
        url = ""
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        print("setup")

    def test_01(self):
        '''登录用例，输入正确的账号密码。。。登录成功用例'''
        self.read_element.login("CapUserName", "CapPassWord")
        # 判断结果
        result = self.read_element.is_login_sucess()
        self.assertTrue(result)
        print("登录成功。。。")

    def test_02(self):
        '''登录用例，输入错误的账号密码。。。登录失败用例'''
        self.read_element.login("WapUserName","WapPassWord")
        # 判断结果
        result = self.read_element.is_login_sucess()
        self.assertFalse(result)
        print("登录失败。。。")

    def tearDown(self):
        print("start...")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
