from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
start_url='https://exoplanets.nasa.gov/exoplanet-catalog/'
browser= webdriver.Chrome("/Users/Admin/Desktop/chromedriver_win32")
browser.get(start_url)
time.sleep(10)
def scrape():
    headers=["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planetData=[]
    for i in range(0, 428):
        Soup= BeautifulSoup(browser.page_source, 'html.parser')
        for ul_tag in Soup.find_all('ul', attrs={'class', 'exoplanet'}):
            li_tags= ul_tag.find_all('li')
            temp_list=[]
            for index, li_tag in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tag.find_all('a')[0].contents[0])
                else:
                    try: 
                        temp_list.append(li_tag.find_all[0])
                    except:
                        temp_list.append('')
            planetData.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('scrapper_to.csv', 'w') as f:
        csvwriter= csv.writer(f)
        csv.writer.writerow(headers)
        csvwriter.writerows(planetData)
scraper()