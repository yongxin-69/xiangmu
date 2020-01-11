from base.app_base import AppBase
import page

class PageAppArticle(AppBase):
    # 查找频道
    def page_find_channel(self,channel):
        self.base_app_right_to_left(page.app_area,channel)
    # 查找文章
    def page_find_article(self,article):
        self.base_app_down_to_up(page.app_article,article)
    # 组合业务方法
    def page_app_article(self,channel,article):
        self.page_find_channel(channel)
        self.page_find_article(article)
