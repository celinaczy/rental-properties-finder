import requests
from bs4 import BeautifulSoup
import os

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
property_prices = [property_price.text.replace('\n', '').replace('+/mo', '') for property_price in property_price_tags]
# print(property_prices)

# check if all lists have the same length
print(len(property_links), len(property_addresses), len(property_prices))