import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import time

print("---stock2--------------")
r = requests.get("http://wap.futurewiz.co.kr/dragon/stockgame_rt/starwars202103/detail_transaction/H0000469?charge=yes")
soup = BeautifulSoup(r.content.decode('euc-kr', 'replace'), "html.parser")
items = soup.select("#mainCont > div > table > tbody") #td.lft span.crUp


date = soup.select_one("#mainCont > div > table > tbody > tr:nth-child(2) > td.date.al7")
name = soup.select_one("#mainCont > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > a")
sell = soup.select_one("#mainCont > div > table > tbody > tr:nth-child(2) > td:nth-child(3) > span")
stock = soup.select_one("#mainCont > div > table > tbody > tr:nth-child(2) > td.al > a")
price = soup.select_one("#mainCont > div > table > tbody > tr:nth-child(2) > td:nth-child(9)")

stocklist = []

for item in zip(date, name, sell, stock, price):
    stocklist.append(
        {
            'time' : item[0],
            'name' : item[1],
            'sell' : item[2],
            'stock': item[3],
            'price': item[4]
        }
    )

while True:
    now = datetime.now()
    print(now)
    print(stocklist[0])
    print("---새로고침--------------")
    time.sleep(10)

'''
for item in items:
    temp = []
    time = item.select_one("#mainCont > div > table > tbody > tr:nth-child(2) > td.date.al7").string
    name = item.select_one("#mainCont > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > a").string
    sell = item.select_one("#mainCont > div > table > tbody > tr:nth-child(2) > td:nth-child(3) > span").string
    #mainCont > div > table > tbody > tr:nth-child(2) > td:nth-child(3) > span
    stock = item.select_one("#mainCont > div > table > tbody > tr:nth-child(2) > td.al > a").string
    price = item.select("#mainCont > div > table > tbody > tr:nth-child(2) > td:nth-child(9)")
    # price2 = price.replace(",","")
    # print(price2)
#contentsList > tr:nth-child(1) > td:nth-child(5)
    temp.append(time)
    temp.append(name)
    temp.append(sell)
    temp.append(stock)
    temp.append(price)
stocklist.append(temp)
print(stocklist[0][0]) 
print(stocklist[0][1]) 
print(stocklist[0][2]) 
print(stocklist[0][3]) 
print(stocklist[0][4]) 
'''
print("--------------------------")