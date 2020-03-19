# __Author:"Levente Liu"
from selenium import webdriver
import unittest,time
from test_case.util.read_method import ReadElement
from selenium.webdriver.common.action_chains import ActionChains

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.read_element = ReadElement(self.driver)
        url = "https://gyp.youboy.com/"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        print("setup")

    def test_01(self):
        '''登录商家后台，发布一个新的商品，并在商品列表搜索该商品'''
        # 登录商家后台
        self.read_element.login_g("GUserName", "GPassWord")
        # 切换至商品
        self.read_element.get_user_element("seller").click()
        # 进入发布商品
        self.read_element.get_user_element("release_sp").click()
        # 输入商品名称
        self.read_element.send_user_info("Trade_name","测试商品")
        # 选择商品类目
        # 商品类目：
        self.read_element.get_user_element("input_inner_y").click()
        self.read_element.get_user_element("dropdown_item").click()

        self.read_element.get_user_element("input_inner_e").click()
        self.read_element.get_user_element("el_scrollbar").click()

        self.read_element.get_user_element("input_inner_s").click()
        self.read_element.get_user_element("el_scrollbat").click()
        time.sleep(3)
        # 选择主图
        self.read_element.send_user_info("image",r"C:\Users\Public\Pictures\Sample Pictures\Test.jpg")
        time.sleep(5)
        print("--------")
        # 计量单位
        self.driver.find_element_by_xpath("//*[@id='app']/div/div[3]/section/div/div[2]/form/div[10]/div/div/div/input").click()
        # 商品规格

        # 价格库存


        time.sleep(5)
    def tearDown(self):
        print("start...")
        # self.driver.quit()

if __name__ == '__main__':
    unittest.main()
  