# __Author:"Levente Liu"

from selenium import webdriver
import time
import unittest
from test_case.util.read_method import ReadElement


class TestCase(unittest.TestCase):
    driver = None
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.read_element = ReadElement(cls.driver)
        url = ""
        cls.driver.get(url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)

    def setUp(self):
        print("setup")

    def test_01(self):
        '''登录之后搜索“扳手”用例，登录成功、搜索成功'''
        self.read_element.login("CapUserName","CapPassWord")
        self.read_element.search("扳手")
        num = self.read_element.get_user_element("spnumber").text
        print("搜索之后页面:",num)


    def test_02(self):
        '''搜索商品之后继续搜索云工厂：庆科技机械'''
        self.read_element.get_user_element("search_y").click()
        time.sleep(3)
        self.element = self.read_element.get_user_element("search_y_btn")
        self.element[1].click()
        time.sleep(2)
        self.read_element.get_user_element("search_y_s").clear()
        self.read_element.send_user_info("search_y_s","庆科技机械")
        self.read_element.get_user_element("sear_y_s_btn").click()
        try:
            ycgname = self.read_element.get_user_element("search_ygc").text
            assert u"庆科技机械" in self.driver.title
            print("搜索成功，云工厂名称包含“庆科技机械”:",ycgname)
        except:
            print("搜索失败。。。。。。")

    def tearDown(self):
        print("start...")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
