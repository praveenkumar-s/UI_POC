import sys,os
sys.path.append(os.path.curdir)
from requestium import Session, Keys
from Pages import Home,Signin
from config_vars import driverconfig as dc
s= Session(webdriver_path=dc.webdriver_path,browser=
dc.browser,default_timeout=dc.default_timeout)#, webdriver_options=dc.webdriver_options)

hme= Home.Home_page(s.driver)
hme.reach()
hme.click_AB()
sg= Signin.Sign_in_page(s.driver)
sg.set_state_signin(callback="https://www.blacktickets.in/chennai")
import time

time.sleep(15)

s.driver.quit()