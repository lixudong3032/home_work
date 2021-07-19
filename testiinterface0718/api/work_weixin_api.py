#coding=utf-8
# @Time : 2021/7/19 18:39
# @Author : lixudong
# @Email : lixudong@zsyjr.com
# @File : work_weixin_api.py
import json

import requests


class WorkWeixinApi:
    work_wei_xin=" https://qyapi.weixin.qq.com/"
    corpid="wwa46c703d97fb8bd3"
    ##corpsecret ="grLGmfemCbhR7koeNVPhZ8xNzTwF4YfqqvhGkVbyykg"
    corpsecret = "WGwR7WE6kYFTzg7gy0AfX4o4pNFEtvj9XVynWRZTqBY"

    def __init__(self):
        self.token=self.getToken()

    def getToken(self):
        """
        获取TOKEN值
        :return:
        """
        param={"corpid":self.corpid,
               "corpsecret":self.corpsecret}
        r=requests.request("GET",f"{self.work_wei_xin}cgi-bin/gettoken",params=param)
        return r.json()["access_token"]

  
    def add_contant(self,userid,name,name_alias,mobile,address):
        data={
                "userid": userid,
                "name": name,
                "alias": name_alias,
                "mobile": mobile,
                "department": [1],
                "order":[0],
                "position": "产品经理",
                "gender": "1",
                "is_leader_in_dept": [1],
                "enable":1,
                "telephone": "020-123456",
                "address": address,
                "main_department": 1
              }
        datastr=json.dumps(data,ensure_ascii=False).encode("UTF-8")
        r = requests.request("POST",f"{self.work_wei_xin}cgi-bin/user/create?access_token={self.token}", data=datastr)
        return r

    def update_contant(self,userid,name,address):
        data = {
            "userid": userid,
            "name": name,
            "address": address
        }
        datastr = json.dumps(data, ensure_ascii=False).encode("UTF-8")
        r = requests.request("POST", f"{self.work_wei_xin}cgi-bin/user/update?access_token={self.token}", data=datastr)
        return r;

    def del_contant(self,name_id):
        param = {
            "userid": name_id
        }
        r = requests.request("GET", f"{self.work_wei_xin}cgi-bin/user/delete?access_token={self.token}", params=param)
        return r


    def get_contant(self,name_id):
        param = {
            "userid": name_id
        }
        r = requests.request("GET", f"cgi-bin/user/get?access_token={self.token}", params=param)
        return r