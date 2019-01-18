#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 18:18:38 2019

@author: jeetu
"""

import requests
r=requests.get('https://en.wikipedia.org/wiki/Machine_learning')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content, 'html5lib')
print(r.content)
quotes=[]  # a list to store quotes 
  
table = soup.find('div', attrs = {'id':'container'}) 
  
for row in table.find('div'): 
    quote = {} 
    quote['theme'] = row.h5.text 
    quote['url'] = row.a['href'] 
    quote['img'] = row.img['src'] 
    quote['lines'] = row.h6.text 
    quote['author'] = row.p.text 
    quotes.append(quote) 
  
filename = 'inspirational_quotes.csv'
with open(filename, 'wb') as f: 
    w = csv.DictWriter(f,['theme','url','img','lines','author']) 
    w.writeheader() 
    for quote in quotes: 
        w.writerow(quote) 