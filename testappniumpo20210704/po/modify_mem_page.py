# @Time : 2021/7/6 14:38
# @Author : lixudong
# @File : home_page.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from testappniumpo20210704.po.base_page import BasePage
class ModifyPage(BasePage):
    def del_member(self):
        """
        删除会员
        :return:
        """
        self.driver.find_element_by_xpath("//*[@text='删除成员']").click()
        self.driver.find_element_by_xpath("//*[@text='确定']").click()
        from testappniumpo20210704.po.contant_page import ContantPage
        return ContantPage(self.driver)
