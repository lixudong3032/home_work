# @Time : 2021/7/19 18:37
# @Author : lixudong
# @File : test_work_weixin.py
import pytest
from faker import Faker

from testiinterface0718.api.work_weixin_api import WorkWeixinApi


class TestWorkWeiXin:

    def setup_class(self):
        self.workapi=WorkWeixinApi()
        self.fake = Faker(locale='zh_CN')

    @pytest.fixture()
    def add_content(self):
        print("test...start")
        name = self.fake.name()
        address = self.fake.address()
        user_id = self.fake.random_number()
        print(user_id)
        mobile = "13725551080"
        result = self.workapi.add_contant(user_id, name, name, mobile, address)
        print(result.text)
        return user_id



    def test_add_contant(self):
        """
        案例添加联系人
        :return:
        """
        # 随机生成名字和手机号码
        name = self.fake.name()
        address = self.fake.address()
        user_id=self.fake.random_number()
        print(user_id)
        mobile="15013893228"
        result=self.workapi.add_contant(user_id,name,name,mobile,address)
        assert 0 == result.json()["errcode"]


    def test_update_contant(self,add_content):
        new_name = self.fake.name()
        new_address=self.fake.address()
        name_id=add_content
        result=self.workapi.update_contant(name_id,new_name,new_address)
        print(result.json())
        assert 0 == result.json()["errcode"]


    def test_delete_contant(self,add_content):
        name_id = add_content
        print(name_id)
        result = self.workapi.del_contant(name_id)
        print(result.json())
        assert 0 == result.json()["errcode"]
