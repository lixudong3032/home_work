import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
'''
基础界面主要包括初始化，每个界面基本上都用到
'''
class BasePage:
    login_url="https://work.weixin.qq.com/wework_admin/loginpage_wx"
    home_url="https://work.weixin.qq.com/wework_admin/frame#index"
    debugurl="127.0.0.1:9222"
    is_open_reuse = True
    def __init__(self, dr: WebDriver = None) -> object:
        print("BasePage....start")
        #如果为空，初始化驱动
        if(None==dr):
            ####fase就利用COOIE，进行功能操作
            if self.is_open_reuse==False:
                print("init chrome.......")
                self.dr =webdriver.Chrome()
                self.dr.implicitly_wait(10)
                self.dr.get(self.login_url)
                print(self.dr.get_cookies())
                with open("cookie_data.yml", encoding="UTF-8") as f:
                    logincooke=yaml.safe_load(f)
                    for cooke in  logincooke:
                        self.dr.add_cookie(cooke)
                    self.dr.get(self.home_url)
                print("访问首页成功。。。。。")
            else:
                #true就复用浏览器然后保存cookie
                print("init reuse.......")
                opt = webdriver.ChromeOptions()
                opt.debugger_address = self.debugurl
                self.dr = webdriver.Chrome(options=opt)
                logincooke = self.dr.get_cookies()
                print(logincooke)
                with open("cookie_data.yml", mode="w", encoding="UTF-8") as f:
                    yaml.dump(logincooke, f)
                print("save cookie succefully!!")
        print("BasePage....end")