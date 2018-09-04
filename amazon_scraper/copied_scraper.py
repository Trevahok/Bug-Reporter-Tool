from lxml import html
import csv,os,json
from urllib.request import urlopen
import urllib
from time import sleep
from threading import Thread
import logging
from bs4 import BeautifulSoup as bs

def AmzonParser(url):
    '''requests a webpaege using urllib and parses it to extract data and returns it as json'''
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    try:
        req = urllib.request.Request(url,headers=headers)
        page = urlopen(req).read()
    except Exception as e: 
        print(e) 
        return
    while True:
        sleep(3)
        try:
            doc = html.fromstring(page)
            soup = bs(page)
            PRICES=soup.select_one('#soldByThirdParty > span').text.split()[-1]
            XPATH_NAME = '//h1[@id="title"]//text()'
            XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]//text()'
            XPATH_AVAILABILITY = '//div[@id="availability"]//text()'
 
            RAW_NAME = doc.xpath(XPATH_NAME)
            RAW_CATEGORY = doc.xpath(XPATH_CATEGORY)
            RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)
 
            NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
            CATEGORY = ' > '.join([i.strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
            AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None
 
 
            data = {
                    'NAME':NAME,
                    'CATEGORY':CATEGORY,
                    'PRICES':PRICES,
                    'AVAILABILITY':AVAILABILITY,
                    'URL':url,
                    'ASIN':url.split('/')[-1],
                    }
 
            print(data)
            return data
        except Exception as e:
            print(e)
 
def single_process(AsinNo):
    ''' the single process that is going to threaded. '''
        url = "http://www.amazon.in/dp/"+AsinNo
        print( "Processing: "+url)
        extracted_data=AmzonParser(url)
        logging.info(json.dumps(extracted_data,indent=4))
        logging.info(',')

def process_handler(AsinList):
    '''handles the creation and deletion of threads'''
    thread_list =[]
    for no in AsinList:
        t= Thread(target=single_process, args=[no])
        thread_list.append(t)
        t.start()
        sleep(5)

logging.basicConfig(filename='scraped_data.json',level=logging.INFO,format='%(message)s')

