from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import time

def search(link):
   driver = webdriver.Chrome()
   driver.get("http://www.google.com")
   elem = driver.find_element_by_name("q")
   elem.clear()
   elem.send_keys(link)
   elem.submit()

   time.sleep(3) # wait 3 seconds
   elem1 = driver.find_element_by_css_selector('.Z0LcW.XcVN5d.AZCkJd')

   nyam = elem1.get_attribute("data-tts-text")
   print(nyam)



search('JFK annual passengers 2019')