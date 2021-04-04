import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import time

# html = '''
# <ul>
#     <li> 100 </li> 
#     <li> 200 </li>
# </ul> 
# <ol>
#     <li> 300 </li> 
#     <li> 400 </li>
# </ol>
# '''

# soup = BeautifulSoup(html, 'html5lib')
# result = soup.select('ul li')#:nth-of-type(2)
# for r in result:
#     print(r.text)

r = requests.get("http://starwars.hankyung.com/cast/?refresh=1&id=ALL&trade=0" ).text
soup = BeautifulSoup(r, "html.parser")
items = soup.select("tbody > tr:nth-child(1) > td ") #td.lft span.crUp
tt = soup.select("#contentsList > tr:nth-child(1) > td:nth-child(5) ") #td.lft span.crUp
print("--------------------------")
print(tt)
print("--------------------------")
#hotKeys = soup.select("tbody > tr:nth-child(1) > td:nth-child(2) > a ")

stocklist = []

for item in items:
    temp = []
    name = item.select_one("#contentsList > tr:nth-child(1) > td:nth-child(2) > a")
    sell = item.select_one("#contentsList > tr:nth-child(1) > td:nth-child(3) > span")
    stock = item.select_one("#contentsList > tr:nth-child(1) > td:nth-child(4) > a:nth-child(1)")
    price = item.select("#contentsList > tr:nth-child(1) > td.rgt")
#contentsList > tr:nth-child(1) > td:nth-child(5)
    temp.append(name)
    temp.append(sell)
    temp.append(stock)
    temp.append(price)
    stocklist.append(temp)
#print(stocklist) 

while True:
    now = datetime.now()
    print(now)

    for item1 in items:
        print(stocklist)
    print("---새로고침--------------")
    time.sleep(10)
#print(items)