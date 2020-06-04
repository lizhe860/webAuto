# !/usr/bin/evn python
# -*- coding:utf-8 -*-
# @software: PyCharm
# @time: 2018/11/1 22:10

from common import projectPath
import logging
import time
#1：import  from..import  导入一个模块的时候，Python会先到当前目录下找
# --->找不到的情况 再去Python的环境变量的路径下去找
#定义一个属于自己的日志收集器

class MyLog:
    def my_log(self,level,msg):
        my_logger=logging.getLogger("webAuto")
        my_logger.setLevel("DEBUG")#设置

        #创造一个专属输出渠道  过滤 和排版
        #格式：
        formatter = logging.Formatter('%(asctime)s-%(filename)s-%(name)s-[line:%(lineno)d] %(levelname)s:%(message)s')

        # 1.输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel("INFO")#设置输出级别  大写
        ch.setFormatter(formatter)

        # 文件名称所加的时间格式
        curTime = time.strftime("%Y-%m-%d", time.localtime())

        # 2.输出到指定文件
        fh=logging.FileHandler(projectPath.logs_path+"//WEbAutotestlog_{0}.log".format(curTime),encoding='UTF-8')
        fh.setLevel("INFO")#设置输出级别  大写
        fh.setFormatter(formatter)

        #对接起来 给日志收集器添加一个渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='CRITICAL':
            my_logger.critical(msg)

        # #渠道要记得移除掉 否则 日志输出会重复
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log("DEBGU",msg)

    def info(self,msg):
        self.my_log("INFO",msg)

    def warning(self,msg):
        self.my_log("WARNING",msg)

    def error(self,msg):
        self.my_log("ERROR",msg)

    def critical(self,msg):
        self.my_log("CRITICAL",msg)

if __name__ == '__main__':
    logger=MyLog()
    logger.debug("天啦噜，水滴同学没有见过日志！")#收集
    logger.info("小场面 ，不要慌！")#print
    logger.warning("这么巧，Monica陪着水滴没见过日志！")
    logger.error("华华要生气了！")
    # logger.critical("讲了100遍，还不懂，华华要奔溃了！")


#升级点：自行去思考和拓展
#日志级别 logger name 输出格式  可不可以做成可配置的