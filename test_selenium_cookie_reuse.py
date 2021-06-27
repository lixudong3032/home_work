import time

from selenium import webdriver
import yaml
'''
功能实现说明：
利用复用功能实现企业微信增加管理员的功能；主要难点在于绕过登录技术，定位元素过期；
实现步骤如下：
1.命令行打开谷歌复用窗口----前提是谷歌浏览器已经配置好配置变量:chrome --remote-debugging-port=9222
2.复用窗口的浏览器访问企业微信并且登录。
3.利用pytest,selenium的复用功能采集登录的COOKIE到YML文件。
4.利用YML文件的cookie，pytest,seleniem等操作浏览器-绕过登录，然后进行用户添加，然后验证。
'''
class  TestGetCookieReuse():

    def setup(self):
        print("start.....")
        self.env="qa"

    def teardown(self):
        print("end......")
        print(self.env)

    '''
    利用pytest,selenium的复用功能采集登录的COOKIE到YML文件。
    '''
    def test_fuyong_and_save_cookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        dr = webdriver.Chrome(options=opt)
        dr.get("https://work.weixin.qq.com/wework_admin/frame")
        dr.find_element_by_id("menu_contacts").click()
        logincooke = dr.get_cookies()
        print(logincooke)
        with open("cookie_data.yml", mode="w", encoding="UTF-8") as f:
            yaml.dump(logincooke, f)
        print("save cookie succefully!!")
        pass

    '''
    3.利用pytest,selenium的复用功能采集登录的COOKIE到YML文件。
    4.利用YML文件的cookie，pytest,seleniem等操作浏览器-绕过登录，然后进行用户添加，然后验证。
    '''
    def test_loadcookie(self):
        self.dr=webdriver.Chrome()
        self.dr.implicitly_wait(10)
        self.dr.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        print(self.dr.get_cookies())
        #打开文件复用cookie
        with open("cookie_data.yml", encoding="UTF-8") as f:
            logincooke=yaml.safe_load(f)
            for cooke in  logincooke:
                self.dr.add_cookie(cooke)
        self.dr.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.dr.find_element_by_id("menu_contacts").click()
        try:
            menu=self.dr.find_elements_by_css_selector("[class='qui_btn ww_btn js_add_member']")[1]
            menu.click()
        except:
            #元素过期导致不能点击，界面刷新一下
            self.dr.refresh()
            time.sleep(5)
            self.dr.find_elements_by_css_selector("[class='qui_btn ww_btn js_add_member']")[1].click()
        self.add_contant("测试人")
        result=self.is_exit("测试人")
        #简单验证是否可以在表格查询的到
        self.assertTrue(result)



    '''
    界面添加联系人
    '''
    def add_contant(self,testname):
        self.dr.find_element_by_id("username").send_keys(testname)
        self.dr.find_element_by_id("memberAdd_english_name").send_keys("testlixudong")
        self.dr.find_element_by_id("memberAdd_acctid").send_keys("lixudongtest1only")
        self.dr.find_element_by_id("memberAdd_mail").send_keys("5034844@qq.com")
        self.dr.find_elements_by_css_selector("[class='qui_btn ww_btn js_btn_save']")[1].click()

    '''
    界面是否可以查询的到联系人
    '''
    def is_exit(self,testname):
        try:
            self.dr.find_element_by_xpath("//table//tbody[@id='member_list']//td[@title='"+testname+"']")
            return True
        except :
            return False


