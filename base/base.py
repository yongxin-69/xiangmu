# base页面  封装公共方法
import allure

from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog

log = GetLog.get_logger()

class Base:

    # 初始化 driver
    def __init__(self,driver):
        log.info("正在初始化driver: {}".format(driver))
        self.driver = driver
    # 查找元素
    def base_find(self,loc,timeout=60,poll=0.5):
        # 设置显示等待
        log.info("正在查找元素: {}".format(loc))
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    def base_finds(self, loc, timeout=60, poll=0.5):
        # 设置显示等待
        log.info("正在查找元素列表: {}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    # 输入方法
    def base_input(self,loc,text):
        log.info("正在清空元素: {}".format(loc))
        self.base_find(loc).clear()
        log.info("正在给 {} 元素执行输入操作: {}".format(loc,text))
        self.base_find(loc).send_keys(text)
    # 点击方法
    def base_click(self,loc):
        log.info("正在点击 {} 元素 ".format(loc))
        self.base_find(loc).click()
    # 获取文本方法
    def base_get_text(self,loc):
       return self.base_find(loc).text

    # 截图
    def base_get_img(self):
        log.error("出现异常,正在执行截图操作")
        self.driver.get_screenshot_as_file("./images/err.png")
        self.__base_write_img()
    # 图片写入
    def __base_write_img(self):
        with open ("./images/err.png","rb") as f:
            allure.attach("断言错误:",f.read(),allure.attach_type.PNG)

