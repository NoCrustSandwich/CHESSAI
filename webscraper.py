import requests
from bs4 import BeautifulSoup


from selenium import webdriver

# Initialize a headless Chrome browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run headless (without a visible browser window)
driver = webdriver.Chrome(options=options)

# Load the Chess.com page
url = "https://www.chess.com/play/computer/Duo"
driver.get(url)

# Wait for the board to load (you may need to adjust the wait time)
import time
time.sleep(5)

# Get the HTML content after the board is loaded
html_content = driver.page_source

print(html_content)