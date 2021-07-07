import requests
import MySQLdb
from bs4 import BeautifulSoup
import re

def parse(url):
    #URL to be scraped
    url_to_scrape = url
    #Load html's plain data into a variable
    plain_html_text = requests.get(url_to_scrape)
    #parse the data
    soup = BeautifulSoup(plain_html_text.text, "html.parser")
    description_tag = soup.find('div', {'class': 'mw-parser-output'})
    description_list = description_tag.find_all('p')
    description = description_list[1].get_text() +  description_list[2].get_text()

    table_body=soup.find('table', {'class': 'infobox biota'})
    rows = table_body.tbody.find_all('tr')

    kingdom_row = rows[8].find_all('td')
    kingdom = kingdom_row[1].get_text()
        
    phylum_row = rows[9].find_all('td')
    phylum = phylum_row[1].get_text()

    # species_row = rows[14].find_all('td')
    # species = species_row[1].get_text()

    conservation = soup.find('a', {'class': 'mw-redirect'})
    conservation_status = conservation.get_text()
        
    image_tag = soup.find('a', {'class': 'image'})
    image_url = (image_tag.attrs['href'])
    pattern = re.compile('([^\/]+$)')
    image_lasturl = pattern.findall(image_url)
    image_full_url = url + "#/media/" + image_lasturl[0]

    return description, kingdom, phylum, conservation_status, image_full_url

