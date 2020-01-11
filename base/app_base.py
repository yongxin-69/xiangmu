from selenium.webdriver.common.by import By

from base.base import Base


class AppBase(Base):
    '''
    app专属方法
    '''
    def base_app_right_to_left(self,ares_loc,find_text):
        # 获取区域元素
        el = self.base_find(ares_loc)
        # 获取区域位置
        location = el.location
        y = location.get("y")
        # 获取元素宽高
        size = el.size
        width = size.get("width")
        height = size.get("height")
        # 计算 start_x,start_y,end_x,end_y
        start_x = width*0.8
        start_y = y + height * 0.5
        end_x = width * 0.2
        end_y = y + height * 0.5
        # z组合 find_text包含的元素
        loc = By.XPATH,"//*[@class='android.widget.HorizontalScrollView']//*[contains(@text,'{}')]".format(find_text)
        # 首先查找元素
        page_source = self.driver.page_source
        while True:
            try:
                el = self.base_find(loc,timeout=2)
                print("找到指定频道")
                el.click()
                break
            except:
                print("未找到指定频道")
                self.driver.swipe(start_x,start_y,end_x,end_y,2000)
            if page_source == self.driver.page_source:
                print("已到最后一页")
                raise Exception
            else:
                page_source = self.driver.page_source
    def base_app_down_to_up(self,ares_loc,find_text):
        el = self.base_find(ares_loc)
        # 获取元素宽高
        size = el.size
        width = size.get("width")
        height = size.get("height")
        # 计算 start_x,start_y,end_x,end_y
        start_x = width * 0.5
        start_y = height * 0.85
        end_x = width * 0.5
        end_y = height * 0.15
        loc = By.XPATH, "//*[@bounds='[0,390][1080,1716]']//*[contains(@text,'{}')]".format(find_text)
        page_source = self.driver.page_source
        while True:
            try:
                el = self.base_find(loc, timeout=2)
                print("正在查找文章标题{}".format(find_text))
                print("找到指定文章")
                el.click()
                break
            except:
                print("未找到指定文章")
                self.driver.swipe(start_x, start_y, end_x, end_y, 2000)
            if page_source == self.driver.page_source:
                print("已到最后一页")
                raise Exception
            else:
                page_source = self.driver.page_source

