# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.carpages.ca/used-cars/search/?category_id=5'
page=requests.get(url)
html=BeautifulSoup(page.text,'lxml')

df=pd.DataFrame({'Link':[''],'Title':[''],'Price':[''],'Distance':[''],'Colour':[''],'Store':[''],'City':['']})

c=0
while c<10:
    for i in html.find_all('div',class_='media soft push-none rule'):
        link=i.find('a').get('href')
        full_link='https://www.carpages.ca/'+link
        title=i.find('div',class_='media__content').find('a').text
        price=i.find('strong',class_='delta').text.strip() 
        distance=''.join([j.text for j in i.find_all('span',class_='number')])
        colour=i.find_all('div',class_='grey l-column l-column--small-6 l-column--medium-4')[1].text.strip() 
        store=i.find('div',class_='l-column l-column--large-4 grey vehicle__card--dealer').find('h5', class_='hN').text
        city=i.find('div',class_='l-column l-column--large-4 grey vehicle__card--dealer').find('p',class_='hN').text
        df=df.append({'Link':full_link,'Title':title,'Price':price,'Distance':distance,'Colour':colour,'Store':store,'City':city},ignore_index=True)

    next_url=html.find('div',class_='rule--top box no-shadow').find('a',class_='nextprev').get('href')
    full_url='https://www.carpages.ca/'+next_url
    page=requests.get(full_url)
    html=BeautifulSoup(page.text,'lxml')
    c=c+1
 
df.shape

