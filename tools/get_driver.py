from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import appium.webdriver
import page
class GetDriver:
    # web 页面 driver
    __driver = None
    # app 页面 driver
    __app_driver = None
    # 获取driver
    @classmethod
    def get_driver(cls,url):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            # 最大化
            cls.__driver.maximize_window()
            # 打开url1
            cls.__driver.get(url)
        return cls.__driver


    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None:
            cls.__driver.quit()
            cls.__driver = None
     # 获取APPdriver
    @classmethod
    def get_app_driver(cls):

        if cls.__app_driver is None:
            cap = {}
            # server 启动参数
            # 设备信息
            cap['platformName'] = 'Android'
            cap['platformVersion'] = '5.1'
            cap['deviceName'] = 'CSX0217728000025'
            # app的信息
            cap['appPackage'] = page.appPackage
            cap['appActivity'] = page.appActivity
            # 中文
            cap['unicodeKeyboard'] = True
            cap['resetKeyboard'] = True
            # 不重置应用
            cap['noReset'] = False
            cls.__app_driver = appium.webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
        return cls.__app_driver
    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver is not None:
            cls.__app_driver.quit()
            cls.__app_driver = None


