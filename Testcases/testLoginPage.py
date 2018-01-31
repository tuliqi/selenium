__author__ = 'liqi'

import unittest
import sys
from selenium import webdriver
from Pages.loginPage import LoginPage

#
class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        print("准备测试")

    def test_login(self):
        driver = self.driver
        assert_title="飞雪智慧公寓平台"
        # 百度网址
        login_Page= LoginPage(driver,base_url="http://weixin.feixuekj.cn/admin/login")
        login_Page.gotoLoginPage()
        login_Page.input_username_text()
        login_Page.input_password_text()
        login_Page.click_login_btn()
        self.assertEqual(login_Page.get_title(), assert_title)

    def tearDown(self):
        self.driver.quit()
        print("end Login")