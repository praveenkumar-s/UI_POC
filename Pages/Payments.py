import sys,os
sys.path.append(os.path.curdir)
from selenium.webdriver.common.by import By
from selenium import webdriver
from config_vars import urls



class webelementfinder:
    def __init__(self,locator,value):
        self.locator=locator
        self.value=value
    def click(self,driver):
        driver.find_element(self.locator,self.value).click()


class payments_common:
    def __init__(self,driver):
        self.driver=driver
        self.url=urls.PAYMENTS_PAGE
    def reach(self,order_id):
        self.driver.get(self.url.format(order_id))

class payments_jt_wallet:
    def __init__(self,driver):
        self.driver=driver
        self.url=None
        self.pay_with_jt_Wallet_head_button=webelementfinder(By.XPATH,"//*[contains(text(),'Pay with  Justickets Wallet')]")
        self.Name=webelementfinder(By.XPATH,'//*[@id="justickets"]/div/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/form/div[1]/input')
        self.Email=webelementfinder(By.XPATH,'//*[@id="justickets"]/div/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/form/div[1]/div[1]/div/div[1]')
        self.Mobile=webelementfinder(By.XPATH,'//*[@id="justickets"]/div/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/form/div[1]/div[2]/div/div[1]')
        self.PayNow=webelementfinder(By.XPATH,'//*[@id="justickets"]/div/div[2]/div/div[3]/div[1]/div[3]/div[1]/div[2]/form/div[3]/span')    

    def click_PayNow(self):
        self.PayNow.click(self.driver)