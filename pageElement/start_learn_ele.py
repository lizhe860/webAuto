# !/usr/bin/evn python
# -*- coding:utf-8 -*-
# @time: 2020/5/31 21:01

from selenium.webdriver.common.by import By

# 开始学习按钮
start_button = (By.XPATH,'/html/body/div[1]/div[2]/div/section/div[1]/div[3]/a')

ppt_ifram = (By.NAME,"task-content-iframe")
# ppt
ppt = (By.XPATH,'//*[@id="activity-ppt-content"]/div/div[1]/img[1]')
# 下一页
next_page = (By.XPATH,'//*[@id="activity-ppt-content"]/div/div[3]/a[3]')
# 页数
total = (By.XPATH,'//*[@id="activity-ppt-content"]/div/div[3]/div/span')
# 学过了
learned = (By.XPATH,'//*[@id="learn-btn"]')

# 下一任务
next = (By.XPATH,'//*[@id="modal"]/div/div/div[3]/a')
# ifram
mp4_ifram = (By.TAG_NAME,"iframe")
stop_butt = (By.CLASS_NAME,"vjs-big-play-button")
# 时长
times = (By.XPATH,'//div[@class="vjs-duration-display"]')

# jindu
# jindu = (By.XPATH,'//*[@id="modal"]/div/div/div[2]/div/div[2]/div')
jindu = (By.CLASS_NAME,"color-success")


# 视频时长
mp4_times = (By.CLASS_NAME,'addinfo')
# 下一页
mulu_next_page= (By.CLASS_NAME,"next")
# 播放视频
mp4_start = (By.ID,"ck_player")
# 总页数
pages = (By.XPATH,'//div[@id="pager"]//a')

