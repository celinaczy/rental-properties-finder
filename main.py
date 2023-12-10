import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import re

zillow_link = "https://appbrewery.github.io/Zillow-Clone/"
form_link = "https://forms.gle/S5ubcDPky2sce2Dg9"


response = requests.get(zillow_link)
zillow_webpage = response.text

# setup scraper
soup = BeautifulSoup(zillow_webpage, 'html.parser')

# get property links
property_link_tags = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
property_links = [property_link.get('href') for property_link in property_link_tags]
# print(property_links)

# get property addresses
property_address_tags = soup.find_all("address")
property_addresses = [property_address.text.replace('\n','').replace('  ', '') for property_address in property_address_tags]
#print(property_addresses)

# get property prices
property_price_tags = soup.find_all(class_="StyledPropertyCardDataArea-fDSTNn")
property_prices = [re.sub("[^0-9]", "", property_price.text) for property_price in property_price_tags]
# print(property_prices)

# check if all lists have the same length
# print(len(property_links), len(property_addresses), len(property_prices))

# set up selenium web driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
index = 0
driver.get(form_link)
time.sleep(2)
inputs = driver.find_elements(By.CSS_SELECTOR, value="input.whsOnd.zHQkBf")
n = 0
for i in inputs:
    if i.is_displayed() and i.is_enabled():
        n += 1
        if n ==1:
            i.send_keys(property_addresses[index])
        if n ==2:
            i.send_keys(property_prices[index])
        if n ==3:
            i.send_keys(property_links[index])



