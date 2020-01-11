# web 登录
import page
from base.base import Base
from tools.get_log import GetLog
from time import sleep
log = GetLog.get_logger()

class PageMpLogin(Base):
    # 输入手机号
    def page_input_phone(self,phone):
        self.base_input(page.my_phone,phone)

    # 输入验证码
    def page_input_verify_code(self,code):
        self.base_input(page.my_code, code)

    # 点击登录按钮
    def page_click_login(self):
        self.base_click(page.my_login)

    # 获取 昵称
    def page_get_nickname(self):
        return self.base_get_text(page.my_name)


    # 组合业务方法(测试脚本登录调用)
    def page_mp_login(self,phone,code):
        log.info("正在调用自媒体登录业务, 用户名: {} 密码: {}".format(phone,code))
        self.page_input_phone(phone)
        self.page_input_verify_code(code)
        sleep(1)
        self.page_click_login()

    # 组合业务方法(测试脚本发布文章调用)
    def page_mp_login_2(self,phone="13812345678",code="246810"):
        log.info("正在调用自媒体登录成功业务, 用户名: {} 密码: {}".format(phone,code))
        self.page_input_phone(phone)
        self.page_input_verify_code(code)
        sleep(1)
        self.page_click_login()


