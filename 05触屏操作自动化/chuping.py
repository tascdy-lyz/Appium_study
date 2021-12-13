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




    def test_search(self):
        '''
            方法目标：学习元素的定位
            Demo:
                1、打开雪球APP
                2、打开搜索输入框
                3、输入中文阿里巴巴
                4、选择第一条，点击
                5、获取股价，并判断股价价格>200
        '''
        btn = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        btn.click()

        btn.is_enabled()


        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")

        # print("fggg")
        # sleep(10)
        # self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        sleep(10)


        #current_price = self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text

        #如果该元素出现多个值的话，采用find_elements_by_id 获取到列表里
        current_all_price = self.driver.find_elements_by_id('com.xueqiu.android:id/current_price')
        for  price in current_all_price:
            print(price)
            assert  price > 200






