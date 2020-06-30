# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 12:11:21 2020

@author: chjh9
"""


import requests
import bs4
import csv
import time
import datetime

race_number =1
race_date = datetime.datetime(2017,7,23)
end_date = datetime.datetime(2020,6,1)

while race_date < end_date:
    
    for race_number in range(1,10):
        url='http://race.kra.co.kr/raceScore/ScoretableDetailList.do?meet=1&realRcDate=%s&realRcNo=%d' %(race_date.strftime('%Y%m%d'),race_number)
        html = requests.get(url).text
        
        
        #파싱...저장....
        print(race_date)
        
        
        time.sleep(1)
    
   
    race_date = race_date + datetime.timedelta(days=7)