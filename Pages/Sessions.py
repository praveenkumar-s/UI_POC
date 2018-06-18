import sys,os
sys.path.append(os.path.curdir)
from selenium.webdriver.common.by import By
from selenium import webdriver
from config_vars import urls



class webelementfinder:
    def __init__(self,locator,value):
        self.locator=locator
        self.value=value

class Sessions_page:
    def __init__(self,driver):
        self.driver=driver
        self.url=None
        self.dynamic_Session=webelementfinder(By.XPATH,"//*[contains(@data-reactid,'{0}')]")

    def select_session(self,session_id):
        self.driver.find_element(self.dynamic_Session.locator,self.dynamic_Session.value).click()
    