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

class Seatlayout_page:
    def __init__(self,driver):
        self.driver=driver
        self.url=None
        self.Book_Now=webelementfinder(By.XPATH,'//*[@id="justickets"]/div/div[2]/div/div[2]/div/div[4]/span')
        self.Seat_table=webelementfinder(By.XPATH,'//*[@id="justickets"]/div/div[2]/div/div[3]/div/div[3]/div')   
        self.Dynamic_seat=webelementfinder(By.XPATH,"//*[contains(text(),'{0}')]")
        self.free_seating=webelementfinder(By.XPATH,"//*[contains(@class,'count') and contains(text(),{0}) ]")
    
    def click_seat_by_seatnumber(self,number):
        self.driver.find_element(self.Dynamic_seat.locator,self.Dynamic_seat.value.format(number)).click()

    def select_seats_free_seating(self,number):
        self.driver.find_element(self.free_seating.locator,self.free_seating.value.format(number)).click()
    
    def click_Book_Now(self):
        self.Book_Now.click(self.driver)
    