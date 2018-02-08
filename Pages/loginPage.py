#_*_coding:utf-8_*_
__author__ ='liqi'

from selenium.webdriver.common.by import By
from Pages.basePage import Page
from logPrint.logPrint import feixueLogging
import logging

log=feixueLogging()

class LoginPage(Page):
    #用户名输入框
    login_userame=By.ID,"username"
    #密码输入框
    login_password=By.ID,"password"
    #登录按钮
    login_btn=By.XPATH,"//div/button"

    def __init__(self,driver,base_url="http://weixin.feixuekj.cn/admin/login"):
        Page.__init__(self,driver,base_url)

    def gotoLoginPage(self):
        # print("goto Login Page %s" % self.base_url)
        log.logPrint("goto Login Page %s"% self.base_url, logging.DEBUG)
        self.driver.get(self.base_url)

    def input_username_text(self):
        # print("输入username ")
        log.logPrint("输入username ", logging.DEBUG)
        self.input_text(self.login_userame,"飞寓")

    def input_password_text(self):
        # print("输入password ")
        log.logPrint("输入password ", logging.DEBUG)
        self.input_text(self.login_password,"qazwsx")

    def click_login_btn(self):
        # print("点击 login  按钮")
        log.logPrint("点击 login 按钮 ", logging.DEBUG)
        self.click(self.login_btn)