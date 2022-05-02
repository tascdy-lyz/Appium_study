from appium import webdriver


class Test_WebBrowser():


    def setup(self):
        desired_caps={
            'platformName':'Android',
            'platformVersion' : '6.0',
            'deviceName' :'127.0.0.1:7555',
            'browserName': 'Browser',
            'chromedriverExecutable':'F:\\dev_python\\appiumAuto_Testing_python\\chromedirver\\chromedriver.exe',


        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)


    def test_browser(self):
        self.driver.get("http://m.baidu.com")

        self.driver.find_element_by_css_selector('.index-kw')

        pass
