from selenium import webdriver
from selenium.webdriver.common import by
#//*[contains(@data-reactid,'7bd69832-89e4-440a-ab76-84985bceddd4')]
dr = webdriver.Chrome('/Users/praveenkumar/Documents/Praveen/UI_POM_POC/chromedriver')
dr.get('https://www.justickets.in/chennai')
dr.find_element_by_xpath("//*[contains(@data-reactid,'7bd69832-89e4-440a-ab76-84985bceddd4')]").click()
print 1