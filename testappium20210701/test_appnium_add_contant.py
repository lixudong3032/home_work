from appium import webdriver
from faker import Faker
from  appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

'''
添加联系人操作步骤：
1.打开企业微信应用。
2.点击通讯录
3.点击添加成员
4.手动输入添加
5.输入信息：名字，性别，手机号码（利用Faker随机生成名字和手机号码）
6.点击保存
7.取弹出框内容，验证是否有成功字样
'''
class TestAppniumAddContant:

    def setup(self):
        print("start...")
        ##打开应用
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        #desired_caps['appPackage'] = 'com.android.settings'
        #desired_caps['appActivity'] = 'com.android.settings.Settings'
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
        print("end...")


    def teardown(self):
        pass

    def test_add_contant(self):
        fake = Faker(locale='zh_CN')
        #随机生成名字和手机号码
        name=fake.name()
        mobile=fake.phone_number()
        # print("随机名字:"+fake.name())
        # print("随机地址:"+fake.address())
        # print("随机银行:"+fake.bban())
        # print("随机数字:"+str(fake.random_number()))
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        self.driver.find_element_by_xpath("//*[@text='添加成员']").click()
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.driver.find_element_by_android_uiautomator( 'new UiSelector().resourceId("com.tencent.wework:id/au0")').send_keys(name)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.wework:id/eq7")').send_keys(mobile)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.wework:id/av2")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.wework:id/b2x")').click()
        self.driver.find_element_by_xpath("//*[@text='保存']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")
        ###显示等待Toast出现
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]'))
        tost_text = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        assert "成功" in tost_text




