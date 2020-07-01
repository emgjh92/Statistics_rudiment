
import requests
import bs4
import csv
import time
import datetime
import random

race_number =1
race_date = datetime.datetime(2017,7,23)
end_date = datetime.datetime(2017,8,10)

dataList = []

while race_date < end_date:
    
    for race_number in range(1,10):
        url='http://race.kra.co.kr/raceScore/ScoretableDetailList.do?meet=1&realRcDate=%s&realRcNo=%d' %(race_date.strftime('%Y%m%d'),race_number)
        html = requests.get(url).text
        
        
        #파싱...저장....
        # print(race_date)
        soup = bs4.BeautifulSoup(html,"html.parser")
        tables = soup.select("#contents .tableType2 table")
        #print("테이블 갯수 : " , len(tables))
        trList = tables[0].select("tr")
        
        
        for tr in trList:
            tdList = tr.select("td")
            
            row = []
            
            for td in tdList:
                #print(td.text)
                row.append(td.text)
            
            dataList.append(row)
        
      
    time.sleep(random.randint(100,500)/1000)
   
    race_date = race_date + datetime.timedelta(days=7)
    
    
print("완료!!!!")
#print(dataList)
fd = open("./race.csv","w",newline="",encoding='utf-8')
csvfile = csv.writer(fd)
csvfile.writerows(dataList)
fd.close()