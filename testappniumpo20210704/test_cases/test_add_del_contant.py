# @Time : 2021/7/6 14:35
# @Author : lixudong
# @Email : lixudong@zsyjr.com
# @File : test_add_del_contant.py
import pytest

from testappniumpo20210704.po.home_page import HomePage


class TestOperateContants:
    """
    操作联系人用例类，包括添加联系人，删除联系人

    """
    def setup(self):
        self.homePage = HomePage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name,mobile", [("袁秀秀", '15013893228')])
    def test_add_contant(self,name,mobile):
        """
        添加联系人用例步骤：
        1.启动APP首页-点击通讯录-点击通讯录-添加成员-手动输入成员-添加名字，手机号码，-验证添加成功

        :param name:
        :param mobile: 注意格式
        :return:
        """
        contantPage=self.homePage.goto_contant_page().click_Member().click_menu_input_Member().add_contant_info(name, mobile)
        succinfo=contantPage.get_add_suc_info()
        contantPage.back()
        assert succinfo in "添加成功"

    @pytest.mark.parametrize("name", [("袁秀秀")])
    def test_del_contant(self,name):
        """
        添加联系人用例步骤：
        1.启动APP首页-点击通讯录-点击通讯录-添加成员-手动输入成员-添加名字，手机号码，-验证添加成功

        :param name:
        :param mobile: 注意格式
        :return:
        """
        mems=self.homePage.goto_contant_page().goto_edit_mem_page(name).del_member().get_mems()
        assert name not in  mems