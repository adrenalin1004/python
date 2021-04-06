import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import time


def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)

myToken = "xoxb-1591223889366-1925051753862-eiNR145Pou2GyOgUJB0dzCUx"


#post_message(myToken, "#stock", "slack 테스트")
try:
    while True:
        print("---stock2--------------")
        r = requests.get("http://wap.futurewiz.co.kr/dragon/stockgame_rt/starwars202103/detail_transaction/H0000469?charge=yes") #prime club
        #r = requests.get("http://wap.futurewiz.co.kr/dragon/stockgame_rt/starwars202103/detail_transaction/H0000476?charge=yes") #이화진
        #r = requests.get("http://wap.futurewiz.co.kr/dragon/stockgame_rt/starwars202103/detail_transaction/H0000474?charge=yes", verify=False) #홍광진
        soup = BeautifulSoup(r.content.decode('euc-kr', 'replace'), "html.parser")
        items = soup.select("#mainCont > div > table > tbody") #td.lft span.crUp


        date = soup.select_one("#mainCont > div > table > tbody > tr:nth-child(2) > td.date.al7")
        name = soup.select_one("#mainCont > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > a")
        sell = soup.select_one("#mainCont > div > table > tbody > tr:nth-child(2) > td:nth-child(3) > span")
        stock = soup.select_one("#mainCont > div > table > tbody > tr:nth-child(2) > td.al > a")
        price = soup.select_one("#mainCont > div > table > tbody > tr:nth-child(2) > td:nth-child(9)")

        date2 = date.string
        #print("date2: ",date2,type(date2))

        stocklist = []

        for item in zip(date, name, sell, stock, price):
            now = datetime.now()
            #print("now: ",now, type(now))
            #print("date: ",date, type(date))
            date_conv = datetime.strptime(date2, '%m/%d %H:%M')
            date_conv2 = date_conv.replace(year=2021)
            #print("date_conv2: ",date_conv2, type(date_conv2))

            dd = date_conv2 - now
            #print("dd: date_conv2 - now ",dd, type(dd))
            format_date = now.strftime("%m/%d")
            # stocklist.append(
            #     {
            #         'time' : item[0],
            #         'name' : item[1],
            #         'sell' : item[2],
            #         'stock': item[3],
            #         'price': item[4]
            #     }
            # )
            stocklist.append(date)
            stocklist.append(name)
            stocklist.append(sell)
            stocklist.append(stock)
            stocklist.append(price)
            date_diff = stocklist[0].string
            date_diff_con = date_diff.split(" ")
            date_int = date_diff_con[0]
            # print("date_int: ",date_int, type(date_int))
            # print("format_date: ",format_date, type(format_date))
            # print("date_int=format_date:  ",date_int == format_date)

            if date_conv2 < now :
        #      while True:
                    now = datetime.now()
                    datestr=stocklist[0].string
                    namestr=stocklist[1].string
                    sellstr=stocklist[2].string
                    stockstr=stocklist[3].string
                    pricestr=stocklist[4].string
                    print(now)
                    # print(stocklist[0].string)
                    # print(stocklist[1].string)
                    # print(stocklist[2].string)
                    # print(stocklist[3].string)
                    # print(stocklist[4].string)
                    # print(datestr)
                    # print(namestr)
                    # print(sellstr)
                    # print(stockstr)
                   # print(pricestr)

                    print(datestr+" / "+namestr+" / "+sellstr+" / "+stockstr+" / "+pricestr)
                    print("---새로고침--------------\n")
                    post_message(myToken, "#stock", datestr+" / "+namestr+" / "+sellstr+" / "+stockstr+" / "+pricestr)
                    time.sleep(60)
            else:
                now2 = datetime.now()
                print(now2)
                print("신규매매 없음")
                time.sleep(60)
    time.sleep(60)
except KeyboardInterrupt:
        pass

print("--------------------------")