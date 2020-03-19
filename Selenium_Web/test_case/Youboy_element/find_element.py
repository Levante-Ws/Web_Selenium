# __Author:"Levente Liu"

from test_case.util.read_ini import Readini

class FindElement(object):
    def __init__(self,driver):
        self.driver = driver

    # 获取元素
    def get_element(self,key):
        read_ini = Readini()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        values = data.split('>')[1:]
        value = ""
        for i in range(len(values)):
            if i == 0:
                value = value + values[i]
            else:
                value = value + ">" + values[i]

        try:
            if by == "id":
                return self.driver.find_element_by_id(value)
            elif by == "name":
                return self.driver.find_element_by_name(value)
            elif by == "className":
                return self.driver.find_element_by_class_name(value)
            elif by == "xpaths":
                return self.driver.find_elements_by_xpath(value)
            elif by == "css":
                return self.driver.find_element_by_css_selector(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None
