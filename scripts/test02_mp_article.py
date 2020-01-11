from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog
from tools.read_yaml import resd_yaml

log = GetLog.get_logger()
import pytest

class TestMpArticle:
    # 初始化
    def setup_class(self):
        driver  = GetDriver.get_driver(page.url_mp)
        self.page_in = PageIn(driver)
        self.page_in.page_get_PageMpLogin().page_mp_login_2()
        self.article = self.page_in.page_get_PageMpArticle()


    # 关闭driver
    def teardown_class(self):
        GetDriver.quit_driver()

    # 调用发布文章业务方法
    @pytest.mark.parametrize("title,content,expect",resd_yaml("mp_article.yaml"))
    def test_mp_article(self,title,content,expect):
        self.article.page_publish_article(title,content)
        try:
            assert expect == self.article.page_get_commit_result()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.article.base_get_img()
            raise
