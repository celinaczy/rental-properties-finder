# Data entry job automation - Zillow Scraper
# day 53 of 100 days of Code 
scrapes a website using Beautiful Soup and with Selenium fills in a Google Form with the obtained data

## Prerequisites

Before running the script, ensure you have the following installed:

- Python (version 3.x)
- `requests` library
- `BeautifulSoup` library (from `bs4`)
- `selenium` library

You can install the required Python libraries using pip:
``` 
pip install requests
pip install beautifulsoup4
pip install selenium 
```

## Getting Started

1. Clone or download the repository containing the script.

2. Navigate to the directory where the script is located.

3. Update the `zillow_link` variable to the URL of the Zillow clone webpage from which you want to scrape property data.

4. Update the `form_link` variable to the URL of the Google Form to which you want to submit the property data.

5. Run the script using Python:

`python main.py`


## How it Works

1. The script sends a GET request to the Zillow clone webpage and extracts the HTML content.

2. It then uses BeautifulSoup to parse the HTML content and extract property links, addresses, and prices.

3. After extracting the data, the script sets up a Selenium WebDriver with Chrome to automate form submission.

4. For each property, it fills out the Google Form with the corresponding address, price, and link.

5. Finally, it submits the form and moves to the next property until all properties are processed.

## Notes

- Ensure that the Google Form fields match the order of data extraction in the script (address, price, link).
- Adjust the `time.sleep()` value according to your internet speed and page loading time to prevent errors due to timing issues.
- Make sure to handle any potential captcha or anti-bot mechanisms implemented on the webpage or Google Form to avoid interruptions in the scraping process.

## Disclaimer

This script is for educational purposes only. Scraping websites may violate their terms of service, so use it responsibly and consider obtaining permission from website owners before scraping their data.

