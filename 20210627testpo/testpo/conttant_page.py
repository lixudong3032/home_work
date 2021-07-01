from selenium.webdriver.remote.webelement import WebElement

from testpo.add_part_page import AddPartPage
from testpo.base_page import BasePage


class ContantPage(BasePage):

    def click_add_part(self):
        addBtn:WebElement= self.dr.find_element_by_css_selector("a[class='member_colLeft_top_addBtnWrap js_create_dropdown']")
        addBtn.click()
        addBtn: WebElement = self.dr.find_element_by_css_selector("a.js_create_party")
        addBtn.click()
        return AddPartPage();


    def getparts(self):
        mebs=[]
        webElements=self.dr.find_elements_by_css_selector("#main div.member_container a.jstree-anchor")
        for we in webElements:
            mebs.append(we.text)
        print(mebs)
        return mebs