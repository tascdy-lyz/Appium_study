from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
'''

    本方法是为了去了解 toast弹框定位
    
    toast是短暂的消息提示弹框

'''

class Test_dingwei():



    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        # com.android.settings/com.android.settings.Settings
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'

        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['noReset']='true'
        # desired_caps['resetKeyBoard'] = 'true'
        desired_caps['dontStopAppOnReset']='true'

        desired_caps['']=''
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)


    def test_dingwei(self):
        btn = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        btn.click()



        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")

        ALIBABA_Second_Num = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='dcom.xueqiu.android:id/current_price'")

        print(ALIBABA_Second_Num.text)


    def test_uiselector_dingwei(self):
        '''
            Uiautomator 定位方法
        :return:
        '''

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("button")')
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("button")')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("button")')

    def test_uiautomator_scoll_dingwei(self):
        '''
            滚动查找元素
        '''
        self.driver.page_source
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("市界").instance(0));').click()






    def teardown(self):
        pass