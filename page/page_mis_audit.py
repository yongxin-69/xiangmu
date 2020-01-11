from base.base import Base
from base.web_base import WebBase
import page
from time import sleep
class PageMisAudit(WebBase):
    audit_id = None
    # 点击信息管理
    def page_click_info_manage(self):
        self.base_click(page.mis_info_manage)
        sleep(2)
    # 点击内容审核
    def page_click_content_audit(self):
        self.base_click(page.mis_content_audit)
        sleep(2)
    # 输入文章标题
    def page_input_title(self,title):
        self.base_input(page.mis_title,title)
    # 输入频道
    def page_input_channel(self,channel):
        self.base_input(page.mis_channel,channel)
    # 选择状态-->待审核
    def page_click_status(self):
        self.web_base_click_ul_li(placeholder_text="请选择状态",click_text="待审核")
    # 点击查询按钮
    def page_click_search_btn(self):
        self.base_click(page.mis_search_btn)

    # 点击通过
    def page_click_pass_btn(self):
        self.base_click(page.mis_pass_btn)
    # 点击确认通过
    def page_click_confirm_pass(self):
        self.base_click(page.mis_confirm_pass)
    def page_get_audit_id(self):
        return self.base_get_text(page.mis_audit_id)
    # 组合业务方法
    def page_mis_audit(self,title,channel):
        self.page_click_info_manage()
        self.page_click_content_audit()
        self.page_input_title(title)
        self.page_input_channel(channel)
        self.page_click_status()
        self.page_click_search_btn()
        sleep(3)
        self.audit_id = self.page_get_audit_id()
        self.page_click_pass_btn()
        sleep(2)
        self.page_click_confirm_pass()
    # 断言
    def page_assert_success(self,title,channel):
        sleep(5)
        self.driver.refresh()
        sleep(5)
        self.page_input_title(title)
        self.page_input_channel(channel)
        sleep(2)
        self.web_base_click_ul_li("请选择状态","审核通过")
        self.page_click_search_btn()
        sleep(2)
        self.web_find_element(self.audit_id)

