#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 08:29:40 2017

@author: brendontucker

practice for upwork postings on data mining
"""

import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://georgia.bizhwy.com/businesses.php?c=349').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

#print(soup.find_all('b'))

NameList = list()
for bold in soup.find_all('b'):
    NameList.append(bold.string)

print(NameList)