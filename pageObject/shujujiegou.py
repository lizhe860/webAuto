# !/usr/bin/evn python
# -*- coding:utf-8 -*-
# @time: 2020/5/30 13:12

from selenium import webdriver
from pageElement import login_ele,student_center_ele,start_learn_ele
from time import sleep
from pageObject.base_page import BasePage
from pageObject.login import Login_select_project

class shujujiegou(BasePage):
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

    def learning(self):
        # Login_select_project(BasePage).select_project(student_center_ele.shujujiegou,student_center_ele.shujujiegou_2)
        self.select_project(student_center_ele.shujujiegou,student_center_ele.shujujiegou_2)
        global sign
        sign = True
        try:
            # 点击开始/继续学习按钮
            self.ele_click(start_learn_ele.start_button,'【课程详情】')
        except:
            pass

        while sign == True:

            try:
                # 若为ppt页，点击下一页按钮
                self.switch_to_iframe(start_learn_ele.ppt_ifram,'【PPTifram】')
                # 等待ppt出现
                self.wait_eleVisible(start_learn_ele.ppt,'【PPT】')
                # 获得页数
                total = self.get_eleText(start_learn_ele.total,'【PPT】')
                # 循环点击下一页按钮
                for i in range(0,int(total)+1):
                    self.ele_click(start_learn_ele.next_page,'【PPT-下一页】')
            except:
                # 若为视频页，则等待视频播放结束
                self.switch_to_iframe(start_learn_ele.mp4_ifram,'【视频ifram】')
                import sys, time
                for i in range(1800):
                    sys.stdout.write(str(i)+' ')  # 调用sys在屏幕输出
                    sys.stdout.flush()  # 用flush()刷新，没有这句还是会等到缓存满了或者运行到最后了才会一次性全部显示出来
                    time.sleep(1)  # 停顿5然后继续

            # 退出ifram
            self.exit_iframe()
            # 点击 学过了
            self.ele_click(start_learn_ele.learned,'【课程详情-学过了】')
            sign = 1
            while sign == 1:
                try:
                    # 若出现任务完成提示框，点击下一任务
                    self.ele_click(start_learn_ele.next,'【课程详情-下一任务】')
                except:
                    sign = 0


if __name__ == '__main__':
    t = '12%'
    text = str(t).strip(' ').split('%')
    print(text[0],type(text[0]))