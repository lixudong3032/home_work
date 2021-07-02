from faker import Faker
class TestFaker:

    def setup(self):
        pass


    def teardown(self):
        pass

    def test_faker(self):
        fake = Faker(locale='zh_CN')
        print("随机名字:"+fake.name())
        print("随机地址:"+fake.address())
        print("随机银行:"+fake.bban())
        print("随机数字:"+str(fake.random_number()))