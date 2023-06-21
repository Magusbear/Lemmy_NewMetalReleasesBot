import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def is_integer(input):
    try:
        float(input)
    except ValueError:
        return False
    else:
        return float(input).is_integer()
    
def create_Request(wantedMonth):
    month_list = ["none","january","february","march","april","may","june","july","august","september","october","november","december"]
    if is_integer(wantedMonth) is True:
        monthAsInt = int(wantedMonth)
        wantedMonthString = month_list[monthAsInt]
        return wantedMonthString
    else:
        wantedMonthString = wantedMonth
        return wantedMonthString



# Set up Firefox webdriver in headless mode
# options = Options()
# options.add_argument('-headless')
# driver = webdriver.Firefox(options=options)

# For local testing
def get_html():
    filename = "test.html"
    with open(filename, "r") as file:
        html_content = file.read()
    metalSoup = BeautifulSoup(html_content, "html.parser")
    return metalSoup
# for local Testing

# Need selenium to delay the scraping because the site needs ~5 seconds to load
# driver.get("https://www.metal-archives.com/release/upcoming")
# time.sleep(8)                                                   # 8 secs should be enough time for the site to load
# html = driver.page_source                                       # Scraping the html

# metalSoup = BeautifulSoup(html, "html.parser")                  # Using bs4 to parse the html

# driver.quit()                                                   # Quit selenium

def get_data_list(metalSoup):
    rows = metalSoup.find_all("tr")                                 # Every row of the release list is a "tr" class (named either odd or even)
    data_list = []                                                  # declare our data list for the releases
    for row in rows:                                                # loop through all releases and sort them into the data_list
        cells = row.find_all("td")
        if len(cells) >= 6:
            band = cells[0].find("a").get_text()
            album = cells[1].find("a").get_text()
            release_type = cells[2].get_text()
            genre = cells[3].get_text()
            release_date = cells[4].get_text()
            added_date = cells[5].get_text()
            data_list.append([band, album, release_type, genre, release_date, added_date])
    return data_list

def get_wanted_list(data_list,wantedMonthString,wantedGenre,wantedDay):
    wanted_list = []
    for data in data_list:                                          # loop through data list to find releases and add them to the wanted list
        genre = data[3]
        release_date = data[4]
        if wantedGenre in genre.lower() and wantedDay in release_date.lower() and wantedMonthString in release_date.lower():
            wanted_list.append(data)
    return wanted_list

def get_releaseList(wantedGenre,wantedDay,wantedMonth):
    metalSoup = get_html()
    wantedMonthString = create_Request(wantedMonth)
    data_list = get_data_list(metalSoup)
    wanted_list = get_wanted_list(data_list,wantedMonthString,wantedGenre,wantedDay)
    return wanted_list,wantedMonthString