__author__ = 'liqi'

import unittest
from selenium import webdriver
from Pages.bookSign import BookSign
from Testcases.testLoginPage import TestLoginPage
from time import sleep

class TestBookSignPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        TestLoginPage.test_login(self)

    def test(self):
        self.assertTrue()


    def test_bookSign_nopayBook(self):
        driver = self.driver
        # assert_title="飞雪智慧公寓平台"
        # 百度网址
        booksign_Page= BookSign(driver,base_url="http://weixin.feixuekj.cn/admin/index#?act=roomStatusList")
        sleep(1)
        booksign_Page.gotoBookSignPage()
        sleep(3)
        booksign_Page.click_book_apart_dl()
        booksign_Page.click_book_apart_value()
        sleep(1)
        booksign_Page.click_book_btn()
        sleep(1)
        booksign_Page.input_customer_name()
        booksign_Page.input_customer_phone()
        # booksign_Page.set_checkin_date()
        js="document.getElementById('checkInDate').removeAttribute('readonly')"
        driver.execute_script(js)
        sleep(2)
        booksign_Page.set_checkin_date()
        sleep(2)
        booksign_Page.set_sign_period()
        sleep(2)
        booksign_Page.set_pay_period()
        sleep(5)
        booksign_Page.input_book_rent()
        booksign_Page.click_noPay_book_btn()
        sleep(2)



    def test_bookSign_cancelBook(self):
        driver = self.driver
        # assert_title="飞雪智慧公寓平台"
        # 百度网址
        booksign_Page = BookSign(driver, base_url="http://weixin.feixuekj.cn/admin/index#?act=roomStatusList")
        sleep(1)
        booksign_Page.gotoBookSignPage()
        sleep(1)
        booksign_Page.click_book_apart_dl()
        booksign_Page.click_book_apart_value()
        sleep(2)
        booksign_Page.click_cancel_book_btn()

    def test_bookSign_paymoney(self):
        driver = self.driver
        # assert_title="飞雪智慧公寓平台"
        booksign_Page = BookSign(driver, base_url="http://weixin.feixuekj.cn/admin/index#?act=roomStatusList")
        booksign_Page.gotoBookSignPage()
        sleep(1)
        booksign_Page.click_book_apart_dl()
        booksign_Page.click_book_apart_value()
        sleep(2)
        booksign_Page.click_paymoney_btn()
        sleep(2)

    def test_bookSign_CheckIn(self):
        driver = self.driver
        # assert_title="飞雪智慧公寓平台"
        booksign_Page = BookSign(driver, base_url="http://weixin.feixuekj.cn/admin/index#?act=roomStatusList")
        booksign_Page.gotoBookSignPage()
        sleep(1)
        booksign_Page.click_book_apart_dl()
        booksign_Page.click_book_apart_value()
        sleep(2)
        booksign_Page.click_checkIn_btn()
        sleep(1)
        booksign_Page.set_checkIn_name()
        booksign_Page.set_CheckIn_phone()
        booksign_Page.set_CheckIn_cardId()
        booksign_Page.click_checkIn_save_btn()
        sleep(1)

    def test_bookSign_CheckOut(self):
        driver = self.driver
        # assert_title="飞雪智慧公寓平台"
        booksign_Page = BookSign(driver, base_url="http://weixin.feixuekj.cn/admin/index#?act=roomStatusList")
        booksign_Page.gotoBookSignPage()
        sleep(1)
        booksign_Page.click_book_apart_dl()
        booksign_Page.click_book_apart_value()
        sleep(2)
        booksign_Page.click_checkOut_btn()
        sleep(2)
        booksign_Page.click_checkOut_yes_btn()
        sleep(2)


    def tearDown(self):
        self.driver.quit()
