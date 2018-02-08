#_*_coding:utf-8_*_
__author__ ='liqi'

class Page(object):
    '''
    Page 基类,所有Page都继承该类
    '''
    def __init__(self,driver,base_url):
        self.driver=driver
        self.base_url=base_url
        self.timeout=30

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def input_text(self,loc,text):
        self.find_element(*loc).send_keys(text)

    def click(self,loc):
        self.find_element(*loc).click()

    def get_title(self):
        return self.driver.title

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)


    