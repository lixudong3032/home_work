# @Time : 2021/7/6 14:38
# @Author : lixudong
# @File : home_page.py
from appium.webdriver.common.mobileby import MobileBy

from testappniumpo20210704.po.base_page import BasePage
from testappniumpo20210704.po.contant_page import ContantPage


class HomePage(BasePage):
    """
    主页
    """
    _addresslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")
    def goto_contant_page(self):
        """
        点击导航到通讯录界面
        :return:
        """
        self.find_and_click(*self._addresslist_element)
        return ContantPage(self.driver)
