from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
import pytest
from tools.read_yaml import resd_yaml
from tools.get_log import GetLog
log = GetLog.get_logger()
from time import sleep
class TestMisAudit:

    # 初始化
    def setup_class(self):
        sleep(60)
        driver = GetDriver.get_driver(page.url_mis)
        # 登录
        page_mis = PageIn(driver)
        page_mis.page_get_PageMisLogin().page_login_2()
        self.mis_audit = page_mis.page_get_PageMisAudit()
    # 关闭driver
    def teardown_class(self):
        GetDriver.quit_driver()
    # 测试方法
    def test_mis_audit(self,title=page.article_title,channel=page.arrictle_channel):
        self.mis_audit.page_mis_audit(title,channel)
        try:
            # 断言
            self.mis_audit.page_assert_success(title,channel)
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mis_audit.base_get_img()
            raise