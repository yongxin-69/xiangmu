
# 以下为黑马网址
# 自媒体
# url
from tools.read_yaml import resd_yaml

url_mp = "http://ttmp.research.itcast.cn/#/login"
# 后台管理
url_mis = "http://ttmis.research.itcast.cn/#/"
'''
以下为文章配置
'''
article_title = resd_yaml("mp_article.yaml")[0][0]
arrictle_channel = "数据库"
'''
以下为自媒体配置数据
'''
from selenium.webdriver.common.by import By
# 手机号
my_phone = By.CSS_SELECTOR,'[placeholder="请输入手机号"]'
# 验证码
my_code = By.CSS_SELECTOR,'[placeholder="验证码"]'
# 登录
my_login = By.CLASS_NAME,"el-button--primary"
# 昵称
my_name = By.CLASS_NAME,"user-name"
'''
以下为文章发布配置数据
'''
# 点击内容管理
mp_content_manage = By.XPATH, "//div[@class='menu-wrapper']//*[text()='内容管理']"
# 点击发布文章
mp_publish_article = By.XPATH, "//*[contains(text(),'发布文章')]"
# 输入标题
mp_title = By.CSS_SELECTOR, "[placeholder='文章名称']"
# 输入内容之前要切换iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 输入内容
mp_content = By.CSS_SELECTOR, "#tinymce"
# 选择封面
mp_cover = By.XPATH, "//*[text()='自动']"
# 选择点击请选
mp_select = By.CSS_SELECTOR, "[placeholder='请选择']"
# 点击具体频道
mp_select_database = By.XPATH, "//*[text()='{}']".format(arrictle_channel)
# 点击发表
mp_commit = By.CSS_SELECTOR, ".el-button.filter-item.el-button--primary"
# 获取发表结果
mp_commit_result = By.XPATH, "//*[contains(text(),'成功')]"
'''
以下为后台管理登录页面配置数据
'''
# 账号
mis_username = By.CSS_SELECTOR,'[placeholder="用户名"]'
# 密码
mis_pwd = By.CSS_SELECTOR,'[placeholder="密码"]'
# 登录按钮
mis_login_btn = By.CSS_SELECTOR,'#inp1'
# 昵称
mis_nickname = By.CSS_SELECTOR,".user_info>span"
'''
以下为后台文章审核页面配置数据
'''
# 信息管理
mis_info_manage = By.XPATH,"//*[@class='menu']//*[text()='信息管理']"
# 内容审核
mis_content_audit = By.XPATH,"//*[@class='menu']//*[text()='内容审核']"
# 文章标题
mis_title = By.CSS_SELECTOR,'[placeholder="请输入: 文章名称"]'
# 频道
mis_channel = By.CSS_SELECTOR, '[placeholder="请输入: 频道"]'
# 查询
mis_search_btn = By.CSS_SELECTOR,".find"
# 点击通过
mis_pass_btn = By.XPATH,"//*[text()='通过']//.."
# 点击确认通过
mis_confirm_pass = By.CSS_SELECTOR,'.el-button--primary'
# 获取文章id
mis_audit_id = By.CSS_SELECTOR,'.cell>span'
'''
以下为app包名启动名
'''
appPackage = "com.itcast.toutiaoApp"
appActivity = ".MainActivity t4"
'''
以下为app应用配置数据(登录)
'''
# 用户名
app_username = By.XPATH,"//*[@index ='1' and @class='android.widget.EditText']"
# 验证码
app_pwd = By.XPATH,"//*[@index ='2' and @class='android.widget.EditText']"
# 登录按钮
app_login_btn = By.XPATH,"//*[@index ='4' and @class='android.widget.Button']"
# 判断是否登录成功
app_me = By.XPATH ,"//*[@index = '3' and contains(@text,'我的')]"
'''
以下为查找指定文章配置
'''
app_area = By.XPATH, "//*[@class='android.widget.HorizontalScrollView']"
app_article = By.XPATH,"//*[@bounds='[0,390][1080,1716]']"