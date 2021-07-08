from  appium import webdriver
# @Time : 2021/7/6 19:31
# @Author : lixudong
# @Email : lixudong@zsyjr.com
# @File : base_page.py
import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def log_info(self, message):
        logging.info(message)

    def find(self, by, value):
        self.log_info('find')
        self.log_info(by)
        self.log_info(value)
        # 查找元素
        return self.driver.find_element(by, value)

    def finds(self, by, value):
        self.log_info('finds')
        self.log_info(by)
        self.log_info(value)
        # 查找多个元素
        return self.driver.find_elements(by, value)


    def find_and_click(self, by, value):
        self.log_info('find_and_click')
        # 查找元素之后完成点击操作
        self.find(by, value).click()

    def find_and_sendkeys(self, by, value, text):
        self.log_info('find_and_sendkeys')

        # 查找元素之后完成点击操作
        self.find(by, value).send_keys(text)

    def swipe_find(self, text, num=3):
        self.log_info('swipe_find')
        '''
        1、添加查找次数
        2、添加 查找文本 的输入参数
        3、添加隐式等待的动态设置
        :param text:
        :param num:
        :return:
        '''
        # 滑动查找元素
        # 优化 隐式等待，提高查找速度
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:

                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size['width']
                height = size['height']

                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                duration = 2000

                self.driver.swipe(start_x, start_y, end_x, end_y, duration)

            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了 {i} 次，未找到")

    def get_toast_text(self):
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute('text')
        return result

    def back(self, num=3):
        for i in range(num):
            self.driver.back()
