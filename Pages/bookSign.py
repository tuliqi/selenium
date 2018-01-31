#_*_coding:utf-8_*_
__author__ ='liqi'

from selenium.webdriver.common.by import By
from Pages.basePage import Page
from logPrint.logPrint import feixueLogging
import logging

from selenium.webdriver.support.select import Select

class BookSign(Page):
    #租赁管理菜单
    book_menu=By.XPATH,"/html/body/div[2]/div[2]/div/ul/li[3]/a/span[1]"
    #预订签约
    book_menu2=By.XPATH,"//dd/a[@data-url='roomStatusList']"
    #公寓下拉按钮
    book_apart_dl = By.ID,"schValue1"
    #公寓下拉列表的autotest公寓值
    book_apart_value=By.XPATH,"//select/option[@value='81']"
    #房间号输入框
    book_roomnum=By.ID,"schLike1"
    #查找按钮
    book_search_btn=By.XPATH,"//div/button[@onclick='searchFunc()']"
    #重置按钮

    # 预订签约操作按钮
    book_reset_btn=By.XPATH,"//div/a[@onclick='reloadFunc()']"
    #预订签约按钮
    book_btn=By.XPATH,"//td/button[@onclick='reservation(113,81);']"
    #解除预约按钮
    book_cancel_btn=By.XPATH,"//td/button[@onclick='cancelOrder(113,2);']"
    #确认付款按钮
    book_paymoney_btn = By.XPATH, "//td/button[@onclick='payBill(113);']"
    #办理入住按钮
    book_checkIn_btn=By.XPATH,"//td/button[@onclick='checkIn(113,81);']"
    #办理退房按钮
    book_checkOut_btn=By.XPATH,"//td/button[@onclick='checkOut(113);']"

    # 预订页面
    #客户姓名
    book_customer_name=By.ID,"customerName"
    #客户电话
    book_customer_phone=By.ID,"customerPhone"
    #入住日期
    book_checkin_date=By.ID,"checkInDate"
    # Sign zhouqi
    book_sign_period=By.XPATH,"//div/input[@placeholder='请选择签约周期']"
    #月签
    book_sign_period_yue = By.XPATH, "//*[@id='content-main']/div/div/div/form/div[11]/div/div/dl/dd[1]"
    #Pay Period
    book_pay_period=By.XPATH,"//div/input[@placeholder='请选择缴费周期']"
    #月付
    book_pay_period_yue = By.XPATH, "//*[@id='content-main']/div/div/div/form/div[12]/div/div/dl/dd[1]"
    #每期租金
    book_rent=By.ID,"roomRent"
    #未付费预订按钮
    book_noPay=By.XPATH,"//div/button[text()='未付费预订']"
    # 付费签约按钮
    book_Pay = By.XPATH, "//div/button[text()='付费签约']"

    # 办理入住窗口
    book_checkIn_name=By.ID,"name"
    book_checkIn_phone=By.ID,"phone"
    book_checkIn_cardId=By.ID,"cardId"
    book_checkIn_saveCheckIn_btn=By.XPATH,"//div/button[@onclick='saveCheckIn()']"

    # 办理退房窗口
    book_CheckOut_yes_btn=By.XPATH,"//div/a[text()='确定']"

    def gotoBookSignPage(self):
        print("goto BookSign Page %s" % self.base_url)
        self.click(self.book_menu)
        self.click(self.book_menu2)

    def __init__(self,driver,base_url="http://weixin.feixuekj.cn/admin/index#?act=roomStatusList"):
        Page.__init__(self,driver,base_url)

    def click_book_apart_dl(self):
        print("点击 公寓下拉 按钮")
        self.click(self.book_apart_dl)

    def click_book_apart_value(self):
        print("选择公寓")
        self.click(self.book_apart_value)

    def click_book_btn(self):
        print("点击 预订签约 按钮, 进入签约页面")
        self.click(self.book_btn)

    def input_customer_name(self):
        print("客户姓名")
        self.input_text(self.book_customer_name,"autotest")

    def input_customer_phone(self):
        print("客户电话")
        self.input_text(self.book_customer_phone,"12312341234")

    def set_checkin_date(self):
        print("入住日期")
        self.input_text(self.book_checkin_date,"2017-06-07")

    def set_sign_period(self):
        print("签约周期")
        # self.input_text(self.book_sign_period,"月签")
        self.click(self.book_sign_period)
        self.click(self.book_sign_period_yue)
        # Select(self.driver.find_element_by_id("signCycle"))


    def set_pay_period(self):
        print("缴费周期")
        # self.input_text(self.book_pay_period,"月付")
        self.click(self.book_pay_period)
        self.click(self.book_pay_period_yue)
        # Select(self.driver.find_element_by_id("paymentCycle")).select_by_visible_text("月付")

    def input_book_rent(self):
        print("每期租金")
        self.input_text(self.book_rent,"1000")

    def click_noPay_book_btn(self):
        print("点击未付费预订")
        self.click(self.book_noPay)

    def click_Pay_book_btn(self):
        print("付费签约")
        self.click(self.book_Pay)

    def click_cancel_book_btn(self):
        print("解除预约")
        self.click(self.book_cancel_btn)

    def click_paymoney_btn(self):
        print("确认付款")
        self.click(self.book_paymoney_btn)

    def click_checkIn_btn(self):
        print("办理入住")
        self.click(self.book_checkIn_btn)

    def set_checkIn_name(self):
        print("输入姓名")
        self.input_text(self.book_checkIn_name,"muxi")

    def set_CheckIn_phone(self):
        print("入住人电话号码")
        self.input_text(self.book_checkIn_phone,"15052419502")

    def set_CheckIn_cardId(self):
        print("入住人身份证")
        self.input_text(self.book_checkIn_cardId,"360502199206045611")

    def click_checkIn_save_btn(self):
        print("保存入住信息")
        self.click(self.book_checkIn_saveCheckIn_btn)

    def click_checkOut_btn(self):
        print("办理退房")
        self.click(self.book_checkOut_btn)

    def click_checkOut_yes_btn(self):
        print("办理退房_确定")
        self.click(self.book_CheckOut_yes_btn)