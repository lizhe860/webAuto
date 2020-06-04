# !/usr/bin/evn python
# -*- coding:utf-8 -*-
# @time: 2020/5/30 13:15

from selenium.webdriver.common.by import By

# 账号
username = (By.NAME,"txtUserName")
# 密码
pwd = (By.NAME,"txtPassword")
# 验证码
secode = (By.NAME,"seccode")
# 登录
login_button = (By.XPATH,'//*[@id="form1"]/div[4]/button')

