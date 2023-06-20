import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Set up Firefox webdriver in headless mode
options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

# For local testing
# filename = "test.html"
# with open(filename, "r") as file:
#     html_content = file.read()
# metalSoup = BeautifulSoup(html_content, "html.parser")
# for local Testing

# Need selenium to delay the scraping because the site needs ~5 seconds to load
driver.get("https://www.metal-archives.com/release/upcoming")
time.sleep(8)
html = driver.page_source

metalSoup = BeautifulSoup(html, "html.parser")

driver.quit()

rows = metalSoup.find_all("tr")

data_list = []

for row in rows:
    cells = row.find_all("td")
    
    if len(cells) >= 6:
        band = cells[0].find("a").get_text()
        album = cells[1].find("a").get_text()
        release_type = cells[2].get_text()
        genre = cells[3].get_text()
        release_date = cells[4].get_text()
        added_date = cells[5].get_text()
        data_list.append([band, album, release_type, genre, release_date, added_date])

for data in data_list:
    genre = data[3]
    if "deathcore" in genre.lower():
        print(data)
