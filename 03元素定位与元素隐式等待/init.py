# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep

from appium import webdriver
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0'
desired_caps['deviceName']='127.0.0.1:7555'
# com.android.settings/com.android.settings.Settings
desired_caps['appPackage']='com.xueqiu.android'
desired_caps['appActivity']='.view.WelcomeActivityAlias'
desired_caps['unicodeKeyBoard']='true'
desired_caps['resetKeyBoard']='true'




driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

#隐式等待
driver.implicitly_wait(8)

sleep(10)
ell = driver.find_element_by_id('com.xueqiu.android:id/tv_search')
ell.click()
sleep(10)
el2 = driver.find_element_by_id('com.xueqiu.android:id/search_input_text')
el2.send_keys('alibaba')

sleep(10)
el3 = driver.find_element_by_id('com.xueqiu.android:id/name')
el3.click()