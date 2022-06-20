# @Time : 2021/7/6 14:38
# @Author : lixudong
# @File : home_page.py
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from testappniumpo20210704.po.base_page import BasePage
from testappniumpo20210704.po.mem_page import MemPage
from testappniumpo20210704.po.modify_mem_page import ModifyPage

class ContantPage(BasePage):
    _addmemElement=(MobileBy.XPATH,"//*[@text='添加成员']")
    def click_Member(self):
        """
        导航到添加成员界面
        :return:
        """
        self.find_and_click(*self._addmemElement)
        return MemPage(self.driver)

    def get_add_suc_info(self):
        ###显示等待Toast出现
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]'))
        tost_text = self.find(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        return tost_text

    _eddmemElement=(MobileBy.ID,"com.tencent.wework:id/gup")
    def goto_edit_mem_page(self,name):
        self.find_and_click(*self._eddmemElement)
        self.find_and_click(MobileBy.XPATH, f'//*[@text="{name}"]')
        return ModifyPage(self.driver)


    def exit_editmodel(self,name):
        self.find_and_click(MobileBy.ID,"com.tencent.wework:id/guk")
        return ContantPage(self.driver)
    def get_mems(self):
        """
        获取会员的值
        :return:
        """
        weblements=self.finds(MobileBy.XPATH,"//android.view.ViewGroup/android.widget.TextView")
        mems=[]
        for we in weblements:
            mems.append(we.text)
        return mems
