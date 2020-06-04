# !/usr/bin/evn python
# -*- coding:utf-8 -*-
# @time: 2020/6/2 21:34

from common.projectPath import video_times_txt_path
from pageElement import login_ele, student_center_ele, start_learn_ele
import time,sys
from pageObject.base_page import BasePage

class yingyu(BasePage):
    def login(self):
        # 输入账号
        self.ele_send_keys(login_ele.username, '119093733010098', '【登录-输入账号】')
        # 输入密码
        self.ele_send_keys(login_ele.pwd, '1q2w3e4r', '【登录-输入密码】')
        secode = input("请输入验证码：")
        # 输入验证码
        self.ele_send_keys(login_ele.secode, secode, '【登录-输入验证码】')
        # 点击登录
        self.ele_click(login_ele.login_button)

    def select_project(self, kemu, kemu_2):
        self.login()
        self.switch_to_iframe(student_center_ele.iframe, '【选课页面】')
        # 点击 高等数学(专升本)
        self.ele_click(kemu, '【选课页面】')
        # 点击 高等数学(专升本)(MOOC)
        windows = self.driver.window_handles
        self.ele_click(kemu_2, '【选课页面】')
        # 进入新页面
        self.switch_to_window('new', windows)

    def learning(self):
        self.select_project(student_center_ele.yingyu,student_center_ele.yingyu_2)
        # 获取总页数
        page_eles = self.findElements(start_learn_ele.pages)
        pages = len(page_eles)
        page = 1
        while page < pages:
            # 获取所有视频时长
            eles = self.findElements(start_learn_ele.mp4_times)
            print(eles)
            for i in eles:
                times_str = i.text
                with open(video_times_txt_path, 'r') as f:
                    data = f.read()
                if times_str not in data:
                    print('{}不存在',times_str)
                    with open(video_times_txt_path, 'a+') as f:
                        f.writelines(str(times_str)+'\n')
                    windows = self.driver.window_handles
                    # 点击视频,打开新页面
                    i.click()
                    # 进入视频页
                    self.switch_to_window('new', windows)
                    # 点击视频，开始播放
                    self.ele_click(start_learn_ele.mp4_start,"【开始播放】")
                    # 处理时间
                    st = times_str.split(':')
                    if st[0] != '00':
                        T0 = int(st[0]) * 3600
                    else:
                        T0 = 0
                    if st[1] != '00':
                        T1 = int(st[1]) * 60
                    else:
                        T1 = 0
                    T = T0 + T1
                    for i in range(T):
                        sys.stdout.write("#")  # 调用sys在屏幕输出
                        sys.stdout.flush()  # 用flush()刷新，没有这句还是会等到缓存满了或者运行到最后了才会一次性全部显示出来
                        time.sleep(1)  # 停顿5然后继续
                    # 关闭当前窗口
                    self.driver.close()
                    # 若出现浏览器弹窗则关闭
                    try:
                        self.close_windows_alert()
                    except:
                        pass
                    windows = self.driver.window_handles
                    # 切换至视频目录页
                    self.switch_to_window(windows[-1], windows)
                else:
                    print('视频已看过：',times_str)
            # 进入下一页
            page_eles[page].click()
            page += 1











if __name__ == '__main__':
    with open(video_times_txt_path, 'r') as f:
        data = f.read()
        print(data,type(data))
        if '19' in data:
            print('存在')
        else:
            print('不存在')



