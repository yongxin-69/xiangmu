from base.base import Base
import page
from time import sleep

from tools.get_log import GetLog
log = GetLog.get_logger()
class PageMisLogin(Base):
    # 输入账号
    def page_input_username(self,usernsme):
        self.base_input(page.mis_username,usernsme)
    # 输入密码
    def page_input_pwd(self,pwd):
        self.base_input(page.mis_pwd,pwd)
    # 点击登录按钮
    def page_click_login_btn(self):
        # 改变按钮为可点击状态
        js = "document.getElementById('inp1').disabled=false"
        # 执行js语句
        self.driver.execute_script(js)
        # 点击登录按钮
        self.base_click(page.mis_login_btn)
    # 获取用户名
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)
    # 组合方法
    def page_login(self,username,pwd):
        log.info("正在调用后台登录业务 用户名{},密码{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
    # 组合方法  审核时 调用
    def page_login_2(self,username="testid",pwd="testpwd123"):
        log.info("正在调用后台登录业务,审核文章 用户名{},密码{}".format(username,pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()