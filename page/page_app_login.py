from base.app_base import AppBase
import page
class PageAppLogin(AppBase):
    # 输入用户名
    def page_input_username(self,username):
        self.base_input(page.app_username,username)
    # 输入密码
    def page_input_pwd(self,pwd):
        self.base_input(page.app_pwd,pwd)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.app_login_btn)
    # 断言
    def page_get_nickname(self):
        try:
            self.base_find(page.app_me,timeout=3)
            return True
        except:
            return False
    def page_app_login(self,usernsme,pwd):
        self.page_input_username(usernsme)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    def page_app_login2(self,usernsme="13812345678",pwd="246810"):
        self.page_input_username(usernsme)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()


