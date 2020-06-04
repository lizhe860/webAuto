# !/usr/bin/evn python
# -*- coding:utf-8 -*-
# @time: 2020/6/3 22:24

from pageElement import login_ele,student_center_ele
from pageObject.base_page import BasePage

class Login_select_project(BasePage):
    def login(self):
        # 输入账号
        self.ele_send_keys(login_ele.username,'119093733010098','【登录-输入账号】')
        # 输入密码
        self.ele_send_keys(login_ele.pwd,'1q2w3e4r','【登录-输入密码】')
        secode = input("请输入验证码：")
        # 输入验证码
        self.ele_send_keys(login_ele.secode,secode,'【登录-输入验证码】')
        # 点击登录
        self.ele_click(login_ele.login_button)

    def select_project(self,kemu,kemu_2):
        self.login()
        self.switch_to_iframe(student_center_ele.iframe,'【选课页面】')
        # 点击 高等数学(专升本)
        self.ele_click(kemu,'【选课页面】')
        # 点击 高等数学(专升本)(MOOC)
        windows = self.driver.window_handles
        self.ele_click(kemu_2,'【选课页面】')
        # 进入新页面
        self.switch_to_window('new', windows)

