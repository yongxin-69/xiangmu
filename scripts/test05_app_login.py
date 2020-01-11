import pytest
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
log = GetLog.get_logger()
from tools.read_yaml import resd_yaml
login = resd_yaml("mp_login.yaml")
login_data = login[0]



class TestAppLogin:
    def setup_class(self):
        # 初始化
        driver = GetDriver.get_app_driver()
        # 实例化
        self.app_login = PageIn(driver).page_get_PageAppLogin()

    def teardown_class(self):
        # guanbidriver
        GetDriver.quit_app_driver()
    # @pytest.mark.parametrize("username,pwd",resd_yaml("app_login.yaml"))
    def test_app_login(self,username=login_data[0],pwd=login_data[1]):
        self.app_login.page_app_login(username,pwd)
        try:
            assert self.app_login.page_get_nickname()
        except Exception as e:
            log.error(e)
            self.app_login.base_get_img()
            raise
