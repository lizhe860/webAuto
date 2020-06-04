# !/usr/bin/evn python
# -*- coding:utf-8 -*-
# @time: 2020/5/30 13:28

from selenium.webdriver.common.by import By

iframe = (By.NAME,"mainFrame")
# 高等数学(专升本)
shuxue  = (By.ID,"ContentPlaceHolder1_StudentCourseList1_dlInCourse_HyperLink3_0")
# 二级科目
shuxue_2 = (By.XPATH,'//*[@id="ContentPlaceHolder1_CourseIndex2_ctl01_dlCourseware_HyperLink3_0"]')

# 数据结构
shujujiegou = (By.XPATH,'//*[@id="ContentPlaceHolder1_StudentCourseList1_dlInCourse_HyperLink1_2"]')
shujujiegou_2 = (By.XPATH,'//*[@id="ContentPlaceHolder1_CourseIndex2_ctl01_dlCourseware_HyperLink3_0"]')

# 英语
yingyu = (By.XPATH,'//a[text()="英语(三)"]')
yingyu_2 = (By.XPATH,'//a[text()="英语(三)(多码率)"]')



