# @Time : 2021/7/6 14:38
# @Author : lixudong
# @Email : lixudong@zsyjr.com
# @File : home_page.py
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from testappniumpo20210704.po.base_page import BasePage
from testappniumpo20210704.po.mem_page import MemPage
from testappniumpo20210704.po.modify_mem_page import ModifyPage


class ContantPage(BasePage):

    def click_Member(self):
        self.driver.find_element_by_xpath("//*[@text='添加成员']").click()
        return MemPage(self.driver)

    def get_add_suc_info(self):
        ###显示等待Toast出现
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]'))
        tost_text = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        return tost_text

    def goto_edit_mem_page(self,name):
        self.driver.find_element_by_id("com.tencent.wework:id/gup").click()
        self.driver.find_element(MobileBy.XPATH, f'//*[@text="{name}"]').click()
        return ModifyPage(self.driver)


    def exit_editmodel(self,name):
        self.driver.find_element_by_id("com.tencent.wework:id/guk").click()
        return ContantPage(self.driver)

    def back(self):
        self.driver.find_element_by_id("com.tencent.wework:id/gu_").click()
        return MemPage(self.driver)

    def get_mems(self):
        """
        获取会员的值
        :return:
        """
        weblements=self.driver.find_elements(MobileBy.XPATH,"//android.view.ViewGroup/android.widget.TextView")
        mems=[]
        for we in weblements:
            mems.append(we.text)
        return mems
