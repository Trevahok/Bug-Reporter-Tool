from bs4 import BeautifulSoup as bs 
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import copied_scraper  as scraper_util
import logging
import matplotlib.pyplot as plt
import json
from sys import argv

logging.basicConfig(filename='scraped_data.json',level=logging.INFO,format='%(message)s')

def get_asins():
    words = input('enter the term to search for:')
    web = webdriver.Chrome('/Users/ssvighnesh/chromedriver')  #replace this with an absolute path of a local driver that is downloaded from selenium website
    keywords = '+'.join(words.strip().split())
    web.get('https://www.amazon.in/s?url=search-alias%3Daps&field-keywords=' + keywords)
    page= web.page_source
    soup = bs(page,'lxml')
    things = soup.find_all('li')
    new =[]
    for thing in things:
        if thing.get('data-asin'):
            new.append(thing.get('data-asin'))
    web.close()
    return new


def plot_this():
    with open('scraped_data.json') as df:
        data = '[' + df.read()[:-2] +']'
        data =  json.loads(data)

    data.sort(key = lambda i :float( i['PRICES']))
    names=[i['NAME'] for i in data ] 
    prices = [i['PRICES'] for i in data]
    plt.plot(names,prices)
    plt.show()

try:
    mode = argv[1]
except:
    print('Usage :\n\n python3 new_scraper.py gen_dat \n\n or \n\n python3 new_scraper.py plot_dat \n\n ')
    exit()

if mode == 'plot_dat':
    plot_this()
elif mode=='gen_dat':
    list_of_asins = get_asins()
    scraper_util.process_handler(list_of_asins)
else:
    print('usage : python3 new_scraper.py gen_dat \n\n or \n\n python3 new_scraper.py plot_dat')
    exit()
