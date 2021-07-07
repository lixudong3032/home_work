# @Time : 2021/7/6 14:38
# @Author : lixudong
# @Email : lixudong@zsyjr.com
# @File : home_page.py
from appium.webdriver import WebElement

from testappniumpo20210704.po.add_mem_page import AddMemPage
from testappniumpo20210704.po.base_page import BasePage



class MemPage(BasePage):
    def click_menu_input_Member(self):
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        return AddMemPage(self.driver)


    def back(self):
        self.driver.find_element_by_id("com.tencent.wework:id/gu_").click()
        from testappniumpo20210704.po.contant_page import ContantPage
        return ContantPage(self.driver)