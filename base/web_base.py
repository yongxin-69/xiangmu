from selenium.webdriver.common.by import By
from time import sleep
from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()
class WebBase(Base):
    def web_base_click_ul_li(self,placeholder_text,click_text):
        # 组合placeholder文本元素定位信息
        loc = By.CSS_SELECTOR,"[placeholder='{}']".format(placeholder_text)
        # 查找元素并点击
        log.info("正在点击下拉元素{}".format(loc))
        self.base_click(loc)
        sleep(2)
        # 定位ul>li -->列表
        loc = By.CSS_SELECTOR,"ul>li"
        log.info("正在选择下拉元素{}".format(loc))
        # 遍历text内容等于click_text 条件成立 click
        for el in self.base_finds(loc):
            if el.text == click_text:
                el.click()
                break


    # 判断元素是否存在
    def web_find_element(self,text):
        loc = By.CSS_SELECTOR,"//*[text()={}]".format(text)
        try:
            self.base_find(loc,timeout=3)
            return True
        except:
            return False