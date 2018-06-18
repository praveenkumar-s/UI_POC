import sys,os
sys.path.append(os.path.curdir)
from selenium.webdriver.common.by import By
from selenium import webdriver
from config_vars import urls,variables



class webelementfinder:
    def __init__(self,locator,value):
        self.locator=locator
        self.value=value
    def click(self,driver):
        driver.ensure_element(self.locator,self.value).click()
    def sendkeys(self,driver,value):
        driver.ensure_element(self.locator,self.value).send_keys(value)

class Sign_in_page:
    def __init__(self,driver):
        self.driver=driver
        self.url=urls.MOVIEPASS_URL
        self.dynamic_Session=webelementfinder(By.XPATH,"//*[contains(@data-reactid,'{0}')]")
        self.callbackurl=None
        self.moviepass_contact=webelementfinder(By.ID,'contact')
        self.moviepass_next=webelementfinder(By.ID,'contact_verify')
        self.moviepass_password=webelementfinder(By.ID,'password')
        self.moviepass_signin=webelementfinder(By.ID,'signin_btn')
        self.moviepass_sign_out=webelementfinder(By.XPATH,'/html/body/nav/div/div[2]/ul/li[2]/a')
    def set_callback_url(self,url):
            self.callbackurl=url
    
    def signin(self,email,password):
        self.driver.get(self.url)
        self.driver.find_element(self.moviepass_contact.locator,self.moviepass_contact.value).send_keys(email)
        self.moviepass_next.click(self.driver)
        self.moviepass_password.sendkeys(self.driver,password)
        self.moviepass_signin.click(self.driver)
        
    def signout(self):
        self.driver.get(self.url)
        if('account' in self.driver.current_url ):
            self.moviepass_sign_out.click(self.driver)


    def set_state_signin(self, callback=None):
        if(callback is not None):
            self.set_callback_url(callback)
        if(self.callbackurl==None):
            return
        else:
            self.driver.get(self.url)
            if('account' in self.driver.current_url ):
                self.driver.get(self.callbackurl)
            else:
                self.signin(variables.MOVIEPASS_USER_EMAIL,variables.MOVIEPASS_USER_PASSWORD)
                self.driver.get(self.callbackurl)
    
    def set_state_Signout(self, callback=None):
        if(callback is not None):
            self.set_callback_url(callback)
        if(self.callbackurl==None):
            return
        else:
            self.driver.get(self.url)
            if('account' in self.driver.current_url ):
                self.moviepass_sign_out.click(self.driver)
                self.driver.get(self.callbackurl)
            else:
                self.driver.get(self.callbackurl)
        