# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#1.접속한다...데이터를 모을 사이트에 접속...
#2.특정 위치에 있는 데이터(텍스트)를 뽑아 온다.
#3.저장한다.


#1. 접속...
import requests
import bs4
import csv


xxx = requests.get("https://www.naver.com")

#print(type(xxx))
#print(xxx.text)#동기식 접속 방법 (Ajax는 비동기식)

soup = bs4.BeautifulSoup(xxx.text, "html.parser")

dataTagList = soup.select(".desc")
print(type(dataTagList))
print(dataTagList)
'''
i = 0
for data in dataTagList:
    #print(i," ",data.text) 
    i +=1
'''

fd = open("./aaaa.csv","w",newline="",encoding='utf-8')
csvfile = csv.writer(fd)
i = 0
for data in dataTagList:
    i += 1
    
    datas = []
    datas.append(i)
    datas.append(data.text)
    csvfile.writerow(datas)

fd.close()
    
    
    
    
    
    
    
    
    
    
    
    