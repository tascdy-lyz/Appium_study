from appium.webdriver.webdriver import WebDriver


class Base_page:
    '''
        公共类，封装基本方法
    '''

    # def __init__(self,driver:WebDriver):
    #     self.driver = driver


    def find(self,*args,**kwargs):
        print(type(kwargs))
        for i in kwargs:
            []
        # if by is None:
        #     raise ValueError("please into the value for by")

        self.driver.find_element()
        pass
Base_page().find()