from time import sleep

import pytest
from appium import webdriver



class Test_chuping():

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        # com.android.settings/com.android.settings.Settings
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'


        #desired_caps['unicodeKeyBoard'] = 'true'
        #desired_caps['resetKeyBoard'] = 'true'
        #desired_caps['dontStopnAppOnReset']='true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()






    def test_touchaction(self):

        '''
            学习Appium的 touchaction方法,从A处 移动到 B处

        :return:
        '''
        from appium.webdriver.common.touch_action import TouchAction
        action = TouchAction(self.driver)
        #获取页面的
        width =  self.driver.get_window_rect()['width']
        height = self.driver.get_window_rect()['height']
        x = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1 / 5)

        action.press(x=x,y=y_start).wait(200).move_to(x=1,y=y_end).release().perform()








