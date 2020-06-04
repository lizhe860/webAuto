# !/usr/bin/evn python
# -*- coding:utf-8 -*-
# @time: 2020/5/31 16:30

import os,requests
from PIL import Image
import matplotlib.pyplot as plt
from common.projectPath import img_path

class pictureProcess():
    def donwload_img(self,cookies,url):
        # headers =
        # User-Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"

        response = requests.get(url,cookies=cookies,verify=False)
        if response.status_code == 200:
            # 表示,如果文件名字相同,就删除当前文件,然后再创建一个一样名字的文件
            with open(img_path + '/secode_img.png', 'wb') as f:
                # print('正在下载当前图片: ' + url)
                # 以二进制的方法写入到本地
                f.write(response.content)


    def show_img(self):
        img = Image.open(img_path + '/secode_img.png')
        plt.figure("Image")  # 图像窗口名称
        plt.imshow(img)
        plt.axis('on')  # 关掉坐标轴为 off
        plt.title('image')  # 图像题目
        plt.show()

if __name__ == '__main__':
    pictureProcess().donwload_img("https://www.xjtudlc.com/api.php?op=checkcode&code_len=3&font_size=14&width=64&height=32&font_color=&background=")
    pictureProcess().show_img()