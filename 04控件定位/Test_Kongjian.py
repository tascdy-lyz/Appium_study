from time import sleep

import pytest
from appium import webdriver



class Test_Kongjian():

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
        #desired_caps['dontStopAppOnReset']='true'
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




    def test_search(self):
        '''
               app交互————学习元素的相关属性以继续相关的方法
               Demo:
                   1、打开雪球APP
                   2、定位首页的输入框
                   3、判断输入框是否可用，并查看属性框的name值属性
                   4、打印搜索框这个元素的左上角坐标和它的宽高
                   5、向搜索框中输入alibaba
                   6、判断【阿里巴巴】是否可见
                   7、如果可见，打印“搜索成功”，如果失败，“打印搜索失败”
        '''
        btn = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        #判断元素是否可用
        btn_name_value = btn.get_attribute('name')
        btn.get_attribute('')
        print(f"输入框的name值为{btn_name_value}")
        print(f"输入框的左上角坐标为：{btn.location}")
        print(f"输入框的左上角坐标为：{btn.size}")
        btn_is_enable = btn.is_enabled()
        if btn_is_enable == True:
            btn.click()


            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")


            alibaba_is_display = self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']")
            alibaba_is_display.get_attribute('displayed')
            if alibaba_is_display.is_displayed() == True:
                print("搜索成功")
            else:
                print("搜索失败")



