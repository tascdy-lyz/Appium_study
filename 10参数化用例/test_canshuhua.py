
'''
    本章节主要是对参数化用例的学习

'''
import pytest
from appium import webdriver
from hamcrest import *


class Test_canshuhua():


    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        # com.android.settings/com.android.settings.Settings
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'

        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['dontStopAppOnReset']='true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    @pytest.mark.parametrize('searchkeys,type,desire_price',[
        ('阿里巴巴','09988',100),
        ('小米', '08180', 100),

    ])
    def test_canshuhua(self,searchkeys,type,desire_price):
        '''
            1、打开雪球APP
            2、点击搜索框
            3、搜索阿里巴巴
            4、

        :return:
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()

        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkeys)

        self.driver.keyevent(66)

        actually_price = self.driver.find_element_by_xpath(f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        actually_price = float(actually_price.text)
        print(f"当前价格为为{actually_price}")
        #assert_that(actually_price,greater_than(desire_price))

    def teardwon(self):
        self.driver.back()
        pass