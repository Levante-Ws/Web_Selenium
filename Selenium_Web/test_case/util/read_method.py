# __Author:"Levente Liu"

from test_case.Youboy_element.find_element import FindElement
from test_case.Youboy_element.find_data import FindData
import time

class ReadElement(object):
    def __init__(self,driver):
        self.driver = driver

    def send_user_info(self, key, data):
        user = self.get_user_namepwd(data)
        self.get_user_element(key).send_keys(user)

    # 定位信息，获取element
    def get_user_element(self, key):
        time.sleep(2)
        # 获取所有页面的句柄
        all_h = self.driver.window_handles
        # 切换至新打开的页面
        self.driver.switch_to.window(all_h[-1])
        time.sleep(2)
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取账号、密码
    def get_user_namepwd(self, data):
        find_data = FindData(self.driver)
        user_data = find_data.get_user(data)
        # print(user_data)
        return user_data

    def is_login_sucess(self):
        u'''判断是否获取到登录账户名称'''
        nametext = self.get_user_element("textname").text
        print(nametext)
        if nametext == "Levante。":
            return True
        else:
            return False

    def login(self, user, pwd):
        '''登录买家端'''
        print("---------------调用登录方法")
        time.sleep(3)
        self.get_user_element("go_login").click()
        time.sleep(3)
        # 获取所有页面的句柄
        all_h = self.driver.window_handles
        # 切换至新打开的页面
        self.driver.switch_to.window(all_h[-1])
        self.send_user_info("username", user)
        self.send_user_info("password", pwd)
        self.get_user_element("login").click()
        time.sleep(30)

    def login_g(self, user, pwd):
        '''登录商家后台方法'''
        self.get_user_element("go_login").click()
        # 获取所有页面的句柄
        # all_h = self.driver.window_handles
        # 切换至新打开的页面
        # self.driver.switch_to.window(all_h[-1])
        self.get_user_element("go_login_g").click()
        self.send_user_info("username_y", user)
        self.send_user_info("password_y", pwd)
        self.get_user_element("login_y").click()
        print("---------------登录成功")
        time.sleep(3)

    def search(self,searchs):
        '''搜索商品'''
        self.get_user_element("search_s").click()
        self.send_user_info("search_s",searchs)
        self.get_user_element("search_s_btn").click()

    def search_y(self, sear):
        '''搜索云工厂方法，适用于登录之后搜索'''
        self.get_user_element("search_s_y").click()
        time.sleep(3)
        self.element = self.get_user_element("search_y_btn")
        self.element[1].click()
        time.sleep(2)
        self.get_user_element("sear_y_s").clear()
        self.send_user_info("sear_y_s", sear)
        self.get_user_element("search_y_s_btn").click()
