# !/usr/bin/evn python
# -*- coding:utf-8 -*-
# @time: 2020/5/31 16:31

import os,time

project_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# print(project_path)

img_path = os.path.join(project_path,"common")
# print(img_path)

project_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# print(project_path)
curTime = time.strftime('%Y-%m-%d %H%M%S')

logs_path = os.path.join(project_path,'Outputs','logs')

video_times_txt_path = os.path.join(project_path,'common','video_times.txt')

def picture_path(module_name):
    '''
    :param module_name: 图片所属模块名
    :return:
    '''
    picture_path = os.path.join(project_path,'Outputs','picture',module_name+curTime+'.png')
    return picture_path