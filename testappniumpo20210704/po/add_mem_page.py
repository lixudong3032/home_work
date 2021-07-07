# @Time : 2021/7/6 14:38
# @Author : lixudong
# @Email : lixudong@zsyjr.com
# @File : home_page.py
from testappniumpo20210704.po.base_page import BasePage
class AddMemPage(BasePage):
    def add_contant_info(self, name, mobile):
        """
        :param name: 添加的姓名
        :param mobile: 添加的手机号码
        :return: 返回联系人界面
        """
        self.driver.find_element_by_xpath("//*[@text='姓名　']/../android.widget.EditText").send_keys(name)
        self.driver.find_element_by_xpath("//*[@text='手机号']").send_keys(mobile)
        self.driver.find_element_by_xpath("//*[@text='性别']/../android.widget.RelativeLayout").click()
        self.driver.find_element_by_xpath("//*[@resource-id='android:id/content']//android.widget.TextView[@text='女']/../../../*").click()
        self.driver.find_element_by_xpath("//*[@text='保存']").click()
        from testappniumpo20210704.po.contant_page import ContantPage
        return ContantPage(self.driver)
