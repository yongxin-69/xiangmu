from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog
log = GetLog.get_logger()
from tools.read_yaml import resd_yaml
import pytest

class TestMisLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_driver(page.url_mis)
        # 获取PageMisLogin对象
        self.mis_login = PageIn(driver).page_get_PageMisLogin()

    # 结束
    def teardown_class(self):
        GetDriver.quit_driver()
    # 登录测试方法
    @pytest.mark.parametrize("username,pwd,expect",resd_yaml("mis_login.yaml"))
    def test_mis_login(self,username,pwd,expect):
        # 调用登录业务方法
        self.mis_login.page_login(username,pwd)
        # 断言
        try:
            assert expect in self.mis_login.page_get_nickname()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mis_login.base_get_img()
            # 抛异常
            raise