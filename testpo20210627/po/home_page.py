import yaml
from selenium import webdriver

from testpo20210627.po.base_page import BasePage
from testpo20210627.po.conttant_page import ContantPage


class HomePage(BasePage):
    def init(self,dr=None,is_open_resue=False):
        print("homepage init.......")
        pass

   ##首页通讯录菜单按钮，就去联系人首页
    def go_to_contant_page(self):
        self.dr.find_element_by_id("menu_contacts").click()
        return ContantPage()


