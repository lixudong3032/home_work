import pytest
import time

from testpo.conttant_page import ContantPage
from testpo.home_page import HomePage


class TestAddPart:
    def setup_method(self):
        print("down")
        self.main = HomePage()
        self.contantpage = ContantPage()

    def teardown_method(self):
        pass

    def test_add_part(self):
       parts =self.main.go_to_contant_page().click_add_part().add_part("测试部门","深圳雷啸八方有限公司").getparts()
       assert  "测试部门" in parts

