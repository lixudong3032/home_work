from selenium.webdriver.remote.webelement import WebElement

from testpo.base_page import BasePage


class AddPartPage(BasePage):
    def add_part(self, partname, company):
        self.dr.find_element_by_css_selector("div[id='__dialog__MNDialog__'] input[name='name']").send_keys(partname)
        self.dr.find_element_by_css_selector("div#__dialog__MNDialog__ div.ww_dialog_body").click()
        self.select_part(company)
        self.dr.find_element_by_css_selector("div#__dialog__MNDialog__ a.ww_btn_Blue").click()
        from test.testpo.conttant_page import ContantPage
        return ContantPage()

    def select_part(self, partname):
        self.dr.find_element_by_css_selector("div#__dialog__MNDialog__ span.js_parent_party_name").click()
        self.dr.find_element_by_css_selector("div#__dialog__MNDialog__ a.jstree-anchor").click()





