# __Author:"Levente Liu"
from selenium import webdriver
import time
import random
import unittest
from test_case.util.read_method import ReadElement
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        '''生成一个随机数'''
        cls.suiji = random.randint(10,99999999)
        # 使用随机数与固定内容组合，形成发送内容
        cls.news = "测试数据" + str(cls.suiji)
        cls.Order_Number = None
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.read_element = ReadElement(self.driver)
        url = ""
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        print("setup")

    def test_01(self):
        '''登录之后搜索云工厂“庆科技机械”,点击一个商品进入商品详情，获取商品名称，然后点击客服进入消息中心，发送一条消息'''
        self.read_element.login("CapUserName","CapPassWord")
        self.read_element.search_y("庆科技机械")
        # 点击一个商品进入商品详情
        self.read_element.get_user_element("wares").click()
        # 获取商品名称，并打印
        sp_name = self.read_element.get_user_element("wares_name").text
        print("进入商品详情页面，商品名称为：", sp_name)
        # 点击进入消息中心
        self.read_element.get_user_element("news").click()
        print("准备给商家发送信息。。。。。。")
        self.read_element.get_user_element("input_box").click()
        self.read_element.send_user_info("input_box",self.news)
        time.sleep(5)
        self.read_element.get_user_element("send_out").click()
        time.sleep(3)
        print("成功给商家发送信息：",self.news)

    def test_02(self):
        '''进入卖家中心，判断是否收到刚刚买家发送的消息'''
        self.read_element.login_g("GUserName","GPassWord")
        # 进入聊天消息页面
        self.read_element.get_user_element("Chat_message").click()
        # 获取到所有用户名,并点击“Levante。”用户
        users_name = self.read_element.get_user_element("users_name")
        for i in users_name:
            if i.text == "Levante。":
                i.click()

        # 获取与用户“Levante。”的所有聊天信息
        user_message = self.read_element.get_user_element("User_message")
        existence = None
        # 所有聊天信息中是否有跟test_01中发送的消息
        try:
            for i in reversed(user_message):
                if self.news == i.text:
                    existence = "内容获取成功，与期望值一致:"+i.text
                    break
                else:
                    existence = "内容获取失败，与期望值不一致。。。。。。"
            print(existence)
        except:
            print("----------------------")

    def test_03(self):
        '''将商品加入进货车，再进入进货车结算、提交订单'''
        self.read_element.login("CapUserName", "CapPassWord")
        self.read_element.search_y("庆科技机械")
        try:
            ycgname = self.read_element.get_user_element("search_ygc").text
            assert "庆科技机械" in self.driver.title
            print("搜索成功，云工厂名称包含'庆科技机械':", ycgname)
        except:
            print("搜索失败。。。。。。")
        # 进入云工厂
        self.read_element.get_user_element("go_ygc").click()
        # 点击全部商品
        self.read_element.get_user_element("all_wares").click()
        sp_name = self.read_element.get_user_element("all_wares_name")
        for i in sp_name:
            # print(i.text)
            if i.text == "瓷砖地砖缝隙清理工具开槽器清缝锥美缝剂工具钨钢头":
                i.click()
        # 点击加入进货车
        self.read_element.get_user_element("Freight_truck").click()
        print("已将商品加入进货车。。。。。。")

        # 进入个人中心
        self.read_element.get_user_element("personal").click()
        # 进入进货车
        self.read_element.get_user_element("Go_Freight_truck").click()
        print("已进入进货车页面。。。。。。")
        # 选择第一条商品
        self.read_element.get_user_element("Choice").click()
        # 获取选择的商品名称
        Pre_purchase = self.read_element.get_user_element("Pre_purchase").text
        print("已选择的商品名称为：",Pre_purchase)
        # 结算,提交订单
        self.read_element.get_user_element("Settlement").click()
        self.read_element.get_user_element("place_order").click()
        # 获取订单编号
        self.Order_Number = self.read_element.get_user_element("Order_Number").text
        print("提交订单后的订单编号:",self.Order_Number)
        # 进入商家后台
        self.driver.quit()
        self.driver = webdriver.Chrome()
        url = ""
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.get("")
        self.read_element = ReadElement(self.driver)
        self.read_element.login_g("GUserName","GPassWord")
        self.read_element.get_user_element("Order").click()
        self.read_element.send_user_info("Input_order",self.Order_Number)
        self.read_element.get_user_element("Query_order").click()

        try:
            Actual_Order_Number = self.read_element.get_user_element("Actual_Order_Number").text
            print("订单列表查询出了订单号：", Actual_Order_Number)
            if Actual_Order_Number == self.Order_Number:
                print("搜索成功，订单号与期望值一致")
            else:
                print("搜索失败，订单号与期望值不一致")
            time.sleep(5)
        except:
            print("搜索失败，未按指定订单号搜索出内容。。。。。。")

    def tearDown(self):
        self.driver.quit()
        print("start...")

if __name__ == '__main__':
    unittest.main()

