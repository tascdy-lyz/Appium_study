from appium import webdriver
from faker import Faker
from selenium.common.exceptions import NoSuchElementException
import pytest

class Test_qiyevx:

    '''
        setup_class 在一个类中只执行一次
    '''
    def setup_class(self):
        self.faker = Faker('zh-CN')


    def setup(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        # com.android.settings/com.android.settings.Settings
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps["settings[waitForidleTimeout]"] = 0
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)



    @pytest.mark.parametrize
    def test_qiyevx(self):
        '''
            1、打开 【企业微信】应用
            2、进入【工作台】
            3、点击【打卡】
            4、选择 【外出打卡】tab
            5、点击 【第N次打卡】
            6、验证【外出打卡成功】
            7、退出【企业微信】应用

        :return:
        '''
        name = self.faker.name()

        self.driver.get_window_size()
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()
        #滚动查找元素
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
            'scrollIntoView(new UiSelector().text("打卡").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='外出打卡']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'次外出')]").click()


    def test_fengzhuang(self):
        '''
            封装滑动
        :return:
        '''
        num =3
        while True:
            try:
                return  1
            except NoSuchElementException:
                print("未找到，滑动")

                self.driver.swipe()
                pass

    def teardown(self):
        pass