import requests
import MySQLdb
from bs4 import BeautifulSoup
import re
from predict import *
from wiki_urls import *

def parse(url):
    #URL to be scraped
    url_to_scrape = url
    #Load html's plain data into a variable
    plain_html_text = requests.get(url_to_scrape)
    #parse the data
    soup = BeautifulSoup(plain_html_text.text, "html.parser")
    description_tag = soup.find('div', {'class': 'mw-parser-output'})
    description_list = description_tag.find_all('p')
    description = description_list[1].get_text() 
    if len(description_list)>2:
        description += description_list[2].get_text()

    table_body=soup.find('table', {'class': 'infobox biota'})
    if table_body is None:
        table_body = soup.find('table', {'class': 'infobox biota biota-infobox'})
    rows = table_body.tbody.find_all('tr')

    classification = soup.find('a', {'title': 'Taxonomy (biology)'})
    print(classification.get_text())
    info = []
    for row in rows:
        info.append(row.get_text().replace('\n', ' ').strip())

    return description, info

for url in all_urls:
    print(url)
    parse(url)
    print('done')