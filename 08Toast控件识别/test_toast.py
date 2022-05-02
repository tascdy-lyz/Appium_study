from appium import webdriver


class Test_Toast():



    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        # com.android.settings/com.android.settings.Settings
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = '.view.PopupMenu1'
        desired_caps['noReset'] = 'true'

        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)



        pass

    def test_toast(self):
        pass

    def teardown(self):

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Make a Popup!")').click()
        pass

        self.driver.find_element_by_id('android:id/title').click()
        self.driver.find_elements_by_xpath()