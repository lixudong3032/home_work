# @Time : 2021/7/8 10:59
# @Author : lixu
# @File : app.py
from appium import webdriver

from testappniumpo20210704.po.base_page import BasePage
from testappniumpo20210704.po.home_page import HomePage


class App(BasePage):
    def start(self):
        if self.driver==None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.WwMainActivity'
            desired_caps['skipServerInstallation'] = 'true'
            desired_caps['skipDeviceInitialization'] = 'true'
            desired_caps['dontStopAppOnReset'] = 'true'  # 不关闭应用
            desired_caps['autoGrantPermissions'] = 'true'  # 自动获取权限
            desired_caps['noReset'] = 'true'            ##不清除会话记录
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(20)
        else:
            print('driver != None 复用driver')
            # launch_app() 帮我启动应用
            # start_activity 可以启动任何应用
            # self.driver.start_activity()
            self.driver.launch_app()
        return self


    def restart(self):
        self.driver.close()
        self.driver.launch_app()

    def quit(self):
        self.driver.quit()

    def goto_main(self):
        # 进入主页 入口
        return HomePage(self.driver)




