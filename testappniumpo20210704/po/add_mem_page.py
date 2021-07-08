# @Time : 2021/7/6 14:38
# @Author : lixudong
# @Email : lixudong@zsyjr.com
# @File : home_page.py
from appium.webdriver.common.mobileby import MobileBy

from testappniumpo20210704.po.base_page import BasePage
class AddMemPage(BasePage):
    def add_contant_info(self, name, mobile):
        """
        :param name: 添加的姓名
        :param mobile: 添加的手机号码
        :return: 返回联系人界面
        """
        self.find_and_sendkeys(MobileBy.XPATH,"//*[@text='姓名　']/../android.widget.EditText",name)
        self.find_and_sendkeys(MobileBy.XPATH,"//*[@text='手机号']/../android.widget.EditText",mobile)
        self.find_and_click(MobileBy.XPATH,"//*[@text='性别']/../android.widget.RelativeLayout")
        self.find_and_click(MobileBy.XPATH,"//*[@resource-id='android:id/content']//android.widget.TextView[@text='女']/../../../*")
        self.find_and_click(MobileBy.XPATH,"//*[@text='保存']")
        from testappniumpo20210704.po.contant_page import ContantPage
        return ContantPage(self.driver)
