#_*_coding:utf-8_*_
__author__ = 'liqi'

import unittest
from common import HTMLTestRunner
from Testcases.testLoginPage import TestLoginPage
# from Testcases.testBookSign import TestBookSignPage

if __name__ == '__main__':
    TEST_UNIT = unittest.TestSuite()
    # TestLoginPage('test_login'),
    TEST_UNIT.addTest(TestLoginPage('test_login'))
    # testunit.addTest(TestBookSignPage('test_bookSign_nopayBook'))
    # testunit.addTest(TestBookSignPage('test_bookSign_cancelBook'))
    # testunit.addTest(TestBookSignPage('test_bookSign_CheckOut'))
    # 定义报告输出路径
    HTML_PATH = "testReport.html"
    fp = open(HTML_PATH, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"飞雪智慧公寓平台测试", description=u"测试用例结果")
    runner.run(HTML_PATH)
    fp.close()
