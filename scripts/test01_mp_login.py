
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
import pytest
from tools.get_log import GetLog
from tools.read_yaml import resd_yaml
log = GetLog.get_logger()

class TestMpLogin():
    # 初始化

    def setup_class(cls):
        # 获取driver
        cls.driver = GetDriver().get_driver(page.url_mp)
        # 实例化统一入口
        cls.login = PageIn(cls.driver).page_get_PageMpLogin()
    # 关闭驱动

    def teardown_class(cls):
        GetDriver.quit_driver()
    # 测试方法
    @pytest.mark.parametrize("phone,code,expect",resd_yaml("mp_login.yaml"))
    def test_mp_login(self,phone,code,expect ):
        # 调用登录方法
        self.login.page_mp_login(phone,code)
        # 获取昵称 断言
        try:
            assert expect == self.login.page_get_nickname()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.login.base_get_img()


            # 报告
            raise
