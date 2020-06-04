# !/usr/bin/evn python
# -*- coding:utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from common.projectPath import picture_path
from common.my_log import MyLog
import time

logging = MyLog()
class BasePage:
    def __init__(self,driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self,locator,module_name=None,timeout=30,poll_frequency=0.5):
        '''

        :param locator: 元素定位表达式，元组类型。如:(By.xpath,'//div[@class="button"]')
        :param timeout: 等待时长
        :param poll_frequency: 轮询频率
        :param module_name: 等待失败时截图操作，图片文件所需要的模块名称
        :return: None
        '''
        # print('timeout:',timeout,type(timeout))
        if isinstance(locator,tuple):
            try:
                start = time.time()
                WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located(locator))
                end = time.time()
                logging.info('{0}模块等待元素{1}可见，等待时长：{2}'.format(module_name,locator,int(end - start)))
            except:
                logging.error("{0}模块等待元素{1}可见失败".format(module_name,locator))
                # 失败截图
                self.save_picture(__class__.__name__)
                # raise
        else:
            logging.error('{}不是元组类型，请确认参数！'.format(locator))


    # find element
    def findElement(self,locator,module_name):
        if isinstance(locator,tuple):
            try:
                # 等待元素出现
                self.wait_eleVisible(locator,module_name)
                # 查找
                return self.driver.find_element(*locator)
            except:
                logging.error("{}模块查找元素{}失败".format(module_name,locator))
                raise
        else:
            logging.error('{}不是元组类型，请确认参数！'.format(locator))

    # find elements
    def findElements(self, locator, module_name=None):
        if isinstance(locator, tuple):
            try:
                # 等待元素出现
                self.wait_eleVisible(locator, module_name)
                # 查找
                return self.driver.find_elements(*locator)
            except:
                logging.error("{}模块查找元素{}失败".format(module_name, locator))
                raise
        else:
            logging.error('{}不是元组类型，请确认参数！'.format(locator))

    # clear
    def ele_clear(self, locator,module_name=None):
        self.findElement(locator,module_name).clear()   # 查找元素并清空

    # send_keys
    def ele_send_keys(self,locator,value,module_name=None):
        """

        :param locator: locator tuple
        :param value: 输入的数据
        :return:
        """
        ele = self.findElement(locator,module_name)
        try:
            ele.send_keys(value)   # 查找元素并输入
            logging.info("{0}模块:在元素{1}中输入文本{2}".format(module_name,locator,value))
        except:
            logging.error("{0}模块:元素{1}输入操作失败！")
            raise

    # click
    def ele_click(self,locator,module_name=None):
        self.findElement(locator,module_name).click()   # 查找元素并点击

    # 获取元素文本信息
    def get_eleText(self,locator,module_name=None):
        return self.findElement(locator,module_name).text   # 返回文本信息

    # 获取已定位元素的属性值
    def get_eleAttr(self,locator,params,module_name=None):
        '''
        :param locator: locator tuple
        :param params: attr元素属性
        :return:
        '''
        if not isinstance(locator,tuple):
            try:
                ele = self.findElement(locator,module_name)
                value = ele.get_attribute(params)
                logging.info("{0}模块:获取到已定位{1}元素的{2}属性值是{3}".format(module_name,locator,params,value))
                return value
            except:
                logging.error("{0}模块:获取已定位元素的属性值失败")
                raise

    # iframe 切换
    def switch_to_iframe(self,locator,module_name=None,timeout=10,poll_frequency=0.5):
        '''
        :param timeout: 等待时间
        :param locator: iframe定位表达式，by index, name, or webelement.
        :return:
        '''
        if isinstance(locator,tuple):
            try:
                WebDriverWait(self.driver,timeout,poll_frequency).until(EC.frame_to_be_available_and_switch_to_it(locator))
                logging.info("【{}】iframe切换成功".format(module_name))
            except:
                logging.error("【{}】iframe切换失败".format(module_name))
                raise
        else:
            logging.error('{}不是元组类型，请确认参数！'.format(locator))

    # 退出iframe
    def exit_iframe(self):
        try:
            self.driver.switch_to.default_content()
            logging.info("iframe退出成功！")
        except:
            logging.error("iframe退出失败！")
            raise

    # window 切换
    def switch_to_window(self,name,windows=None,timeout=20,poll_frequency=0.5):
        """
            调用此方法前需先获取切换之前的所有窗口，
            windows = self.driver.window_handles
        :param name: new:最新打开的窗口，default：第一个窗口，其他的值表示窗口的handle
        :param windows: 切换之前的所有窗口
        :param timeout: 等待时长
        :return:
        """
        try:
            if name == 'new' and windows is not None:
                logging.info("准备切换至最新的窗口")
                # 等待新窗口出现
                WebDriverWait(self.driver,timeout,poll_frequency).until(EC.new_window_is_opened(windows))
                # 切换到新窗口
                self.driver.switch_to.window(self.driver.window_handles[-1])
            elif name == 'defult':
                logging.info("准备切换至")
                self.driver.switch_to.default()
            else:
                self.driver.switch_to.window(name)
            logging.info("window切换成功！")
        except:
            logging.error("window切换失败！")
            raise

    def __switch_to_window(self, winB):
        """
        :param winB:
            1.切换窗口的标题
            2.切换窗口的序号
            3.切换页面的元素
        :return: True 切换成功
        :Usage:
        driver.switch_to_window('win_name')
        driver.switch_to_window(2) # 切换到第二个窗口
        located=(By.ID,'id') # 确定切换页面的元素
        driver.switch_to_window(located) # 切换到页面中存在located的元素窗口
        """
        result = False
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        if isinstance(winB, tuple):
            for handle in handles:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                try:
                    self.driver.find_element(*winB)
                except :
                    pass
                else:
                    result = True
                    break
            if not result:
                self.driver.switch_to.window(current_handle)
                time.sleep(2)
        elif isinstance(winB, str):
            for handle in handles:
                self.driver.switch_to.window(handle)
                time.sleep(2)
                if winB in self.driver.title:
                    result = True
                    break
            if not result:
                self.driver.switch_to.window(current_handle)
                time.sleep(2)
        elif isinstance(winB, int):
            if winB <= len(handles):
                self.driver.switch_to.window(winB - 1)
                time.sleep(2)
                result = True
        else:
            print('参数错误')
        return result

    # 截图并保存
    def save_picture(self,module_name):
        '''
        :param module_name: 图片所在模块名
        :return:
        '''
        path = picture_path(module_name)
        try:
            self.driver.save_screenshot(path)
            logging.info('{0}截图成功！图片路径为{1}'.format(module_name,path))
        except:
            logging.error('{0}截图失败！'.format(module_name))
            raise

    def close_windows_alert(self):
        alert = Alert(self.driver)
        alert.accept()





