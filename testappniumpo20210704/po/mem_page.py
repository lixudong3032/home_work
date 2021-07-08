# @Time : 2021/7/6 14:38
# @Author : lixudong
# @Email : lixudong@zsyjr.com
# @File : home_page.py
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from testappniumpo20210704.po.add_mem_page import AddMemPage
from testappniumpo20210704.po.base_page import BasePage


class MemPage(BasePage):
    def click_menu_input_Member(self):
        self.find_and_click(MobileBy.XPATH,"//*[@text='手动输入添加']")
        return AddMemPage(self.driver)
