import csv
import unittest
from time import sleep
from selenium import webdriver
from .st_lib import StLib

class St(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.lib = StLib(self.driver)


    # 主函数
    def test_st(self):
        # 读取csv文件到user_list字典类型变量中
        user_list = csv.reader(open("list_to_user.csv","r"))
        # 遍历整个user_list
        for user in user_list:
            sleep(3)
            self.lib.lon_in('admin','admin')
            sleep(2)
            # 断言
            self.assertEqual('http://localhost:8080/index.html',self.driver.current_url,'登陆跳转失败')
            user_to_add = {'account':user[0],
                           'realname':user[1],
                           'gender':user[2],
                           'dept':user[3],
                           'role':user[4],
                           'password':user[5],
                           'email':user[0] + user[6],
                           }
            # 进入后台管理
            self.lib.click_admin_app()
            # 进入嵌套
            self.lib.driver.switch_to.frame('iframe-superadmin')
            sleep(1)
            # 点击添加用户
            self.lib.click_add_user()
            # 退出嵌套
            self.driver.switch_to.default_content()
            sleep(1)
            # 退出
            self.lib.logn_out()
            sleep(2)
            # 用新账号登陆
            self.lib.logn_in(user_to_add['account'],user_to_add['password'])
            sleep(1)
            self.lib.logn_out()
            sleep(1)

    def tearDown(self):
        self.driver.quit()