# __Author:"Levente Liu"

import configparser
import os

class FindData(object):

    def __init__(self,driver,file_name=None):
        self.driver = driver
        if file_name == None:
            file_name = os.path.join(os.getcwd(),"\\config\\RegisterElement.ini")
            # file_name = os.path.join(os.getcwd(),"\config\RegisterElement.ini")
        self.cf = self.load_ini(file_name)

    # 加载文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    # 获取账号、密码
    def get_user(self,data):
        data = data
        # user = ""
        if data == "CapUserName":
            user =  self.cf.get("Cap","name")
        elif data == "CapPassWord":
            user = self.cf.get("Cap","pwd")
        elif data == "WapUserName":
            user = self.cf.get("Wap","name")
        elif data == "WapPassWord":
            user = self.cf.get("Wap","pwd")
        elif data == "GUserName":
            user = self.cf.get("Cap_g","name")
        elif data == "GPassWord":
            user = self.cf.get("Cap_g","pwd")
        else:
            user = data
        return user
#
# if __name__ == '__main__':
#     read_init = FindData()
#     print(read_init.get_user("WapUserName"))

