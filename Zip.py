import time
import xlsxwriter as xlsxwriter
import numpy
from pandas import ExcelWriter
from pandas.compat import numpy
from selenium.webdriver.common import keys
from selenium.webdriver import Keys, DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.devtools.v105 import browser
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pandas as pd

# Reads Zip codes from excel file to convert them into an array to use on a website to webscrape
data = pd.read_excel(r'C:\Users\spain\Desktop\ZIP_Locale_Detail_1.xls', dtype='object')
X = data["PHYSICAL ZIP"]
Zips = X.values
length = len(X)
for x in Zips:
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.get("https://ziplook.house.gov/zip/ziplook.html")
    driver.execute_script("window.open('');")
    input = driver.find_element("name", "zip")
    # print(input)
    input.send_keys(x)  # we can make a loop of some sort to make zip codes find all the representatives here
    # I used 77575 because i live in liberty
    input.send_keys(Keys.ENTER)
    time.sleep(.5)#waits till window is open

    # print every open window page title

    element = driver.find_elements(By.CSS_SELECTOR, '.wide > table:nth-child(6) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > a:nth-child(1)')
    for e in element:
        zip = e.text

        element = driver.find_elements(By.CSS_SELECTOR,'.wide > table:nth-child(6) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2) > a:nth-child(1)')
        for t in element:
            representative = t.text

            element = driver.find_elements(By.CSS_SELECTOR,'.wide > table:nth-child(6) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(3)')
            for b in element:
                stateDistrict = b.text
    driver.close()
    driver.quit()
    Z = representative.replace(" ", "_")
    W = stateDistrict.replace(" ", "_")
    Y = zip.split()
    W = W.split()
    Z = Z.split()
    Z = Y + Z + W
    print(Z)
    df = pd.DataFrame({"Representatives": Z})

        # Naming the columns
    df.index = ['Zipcodes', 'Representatives', 'State/District']

    # Exporting data into Excel
    df.to_csv('result.csv')
