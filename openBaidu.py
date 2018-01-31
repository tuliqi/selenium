#_*_coding:utf-8_*_
__author__='liqi'

import logging
import unittest
from time import sleep

from selenium import webdriver

from common import HTMLTestRunner

logging.basicConfig(level=logging.INFO)

class BaiduTest(unittest.TestCase):
    """百度首页搜索测试用例"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = u"http://www.baidu.com"

    def test_baidu_search(self):
        driver = self.driver
        # print (u"开始[case_0001]百度搜索")
        logging.info("百度搜索")
        driver.get(self.base_url)
        # 验证标题
        self.assertEqual(driver.title, u"百度一下，你就知道")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(u"开源优测")
        driver.find_element_by_id("su").click()
        sleep(3)
        # 验证搜索结果标题
        self.assertEqual(driver.title, u"开源优测_百度搜索")

    def tearDown(self):
        self.driver.quit()

class Login(unittest.TestCase):
    """平台登录测试用例"""

    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.base_url = u"http://weixin.feixuekj.cn/admin/login"

    def test_login(self):
        driver = self.driver
        # print (u"开始[case_0001]百度搜索")
        logging.info("login to platform")
        driver.get(self.base_url)
        # 验证标题
        self.assertEqual(driver.title, u"飞雪科技|登录")
        # x=driver.find_elements_by_xpath("//div/input")
        # logging.info(len(x))
        driver.find_element_by_name("username").send_keys("tuliqi")
        driver.find_element_by_name("password").send_keys("Fx19911213")
        driver.find_element_by_class_name("login-btn").click()
        sleep(3)
        # 验证主界面标题
        logging.info("switch to HomePage")
        self.assertEqual(driver.title, "飞雪物控平台")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Login('test_login'))
    # 定义报告输出路径
    htmlPath = u"testReport.html"
    fp = open(htmlPath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"百度测试", description=u"测试用例结果")
    runner.run(testunit)
    fp.close()