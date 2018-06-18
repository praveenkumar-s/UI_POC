import sys,os
sys.path.append(os.path.curdir)
from config_vars import urls
from selenium.webdriver.common.by import By


class webelementfinder:
    def __init__(self,locator,value):
        self.locator=locator
        self.value=value
    def click(self,driver):
        driver.find_element(self.locator,self.value).click()

class Home_page:
    def __init__(self,driver):
        self.driver=driver
        self.url=urls.HOME_PAGE
        self.Bookins_Open=webelementfinder(By.XPATH,'//*[@id="justickets"]/div/div[2]/div/div[2]/div[2]/div[1]/p')
        self.Assisted_Booking= webelementfinder(By.XPATH,'//*[@id="justickets"]/div/div[2]/div/div[2]/div[2]/div[2]/p')
        self.Offers=webelementfinder(By.XPATH,'//*[@id="justickets"]/div/div[2]/div/div[2]/div[2]/div[3]')
        self.Movietoselect=webelementfinder(By.XPATH,"//*[contains(@data-reactid,'{0}')]")
    def reach(self):
        self.driver.get(self.url)
    def click_AB(self):
        self.Assisted_Booking.click(self.driver)
    def click_Movie(self,moviebuff_id):
        self.driver.find_element(self.Movietoselect.locator,self.Movietoselect.value.format(moviebuff_id)).click()
 


