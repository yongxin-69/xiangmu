from time import sleep

from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestAppArticle:
    def setup_class(self):
        driver = GetDriver.get_app_driver()
        self.page_in = PageIn(driver)
        self.page_in.page_get_PageAppLogin().page_app_login2()
        self.article = self.page_in.page_get_PageAppArticle()
    def teardown_class(self):
        GetDriver.quit_app_driver()
    def test_app_article(self):
        self.article.page_app_article(channel="python",article="Python")
        sleep(10)
