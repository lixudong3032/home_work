from  appium import webdriver
# @Time : 2021/7/6 19:31
# @Author : lixudong
# @Email : lixudong@zsyjr.com
# @File : base_page.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self,wb=None):
        if wb==None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.WwMainActivity'
            desired_caps['skipServerInstallation'] = 'true'
            desired_caps['skipDeviceInitialization'] = 'true'
            desired_caps['dontStopAppOnReset'] = 'true'  #不关闭应用
            desired_caps['autoGrantPermissions'] = 'true' #自动获取权限
            ##不清除会话记录
            desired_caps['noReset'] = 'true'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(20)
        else:
            self.driver=wb


    def swipe_find(self, text, num=5):
        self.log_info('swipe_find')
        '''
        1、添加查找次数
        2、添加 查找文本 的输入参数
        3、添加隐式等待的动态设置
        :param text:
        :param num: 默认为3
        :return:
        '''
        # 滑动查找元素
        # 优化 隐式等待，提高查找速度
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:

                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(20)
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
                self.driver.implicitly_wait(20)
                raise NoSuchElementException(f"找了 {i} 次，未找到")
