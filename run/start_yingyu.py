# !/usr/bin/evn python
# -*- coding:utf-8 -*-
# @time: 2020/6/4 0:05

from selenium import webdriver
from common.pictureProcess import pictureProcess
from pageObject.yingyu import yingyu

class run():
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')

        driver = webdriver.Chrome(chrome_options=option)
        driver.maximize_window()
        driver.get("https://www.xjtudlc.com/")
        cookies_list = driver.get_cookies()
        # print(cookie)
        # print('type',type(cookie))
        cookies = {}  # 初始化cookies字典变量
        for i in cookies_list:
            name, value = i['name'], i['value']
            cookies[name] = value
        # print(cookies)
        img_url = "https://www.xjtudlc.com/api.php?op=checkcode&code_len=3&font_size=14&width=64&height=32&font_color=&background="
        pictureProcess().donwload_img(cookies, img_url)
        pictureProcess().show_img()
        self.driver = driver

    def start_yingyu(self):
        yingyu(self.driver).learning()

if __name__ == '__main__':
    run().start_yingyu()

