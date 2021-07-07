# @Time : 2021/7/6 14:38
# @Author : lixudong
# @Email : lixudong@zsyjr.com
# @File : home_page.py
from testappniumpo20210704.po.base_page import BasePage
from testappniumpo20210704.po.contant_page import ContantPage


class HomePage(BasePage):

    def goto_contant_page(self):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        return ContantPage(self.driver)
