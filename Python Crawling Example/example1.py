from urllib.request import urlopen
#from bs4 import BeautifulSoup
import bs4 
import pandas as pd
from html_table_parser import parser_functions as parser
import datetime
import time
import random
import requests

race_number = 1
#race_date = '20170723'
race_date = datetime.datetime(2017, 7, 23)
end_date = datetime.datetime(2017, 8, 10)


while True : 

    

    time.sleep(random.randint(100, 500)/1000)

    if race_date > end_date:
        break


    strRaceDate = race_date.strftime('%Y%m%d')

    print(strRaceDate)


    url="http://race.kra.co.kr/raceScore/ScoretableDetailList.do?meet=1&realRcDate=%s&realRcNo=%d" %(race_date.strftime('%Y%m%d'),race_number)
    print(url)

    html = requests.get(url).text
    
    #print(html)
    soup = bs4.BeautifulSoup(html , "html.parser")

    temp = soup.find_all('table')
    #print(temp[2])

    p=parser.make2d(temp[2])
    df=pd.DataFrame(p[1:],columns=p[0])

    df.to_csv("./" + strRaceDate + ".csv" , sep="," , na_rep="NaN")


    #print(df)

    data_size = len(df)


    race_date = race_date + datetime.timedelta(days=7)



print("완료!!!!!!!!!!!!!!!!!!!!!!!!!")

