from random import randrange
from typing import NewType

print(dir(typing))
def lotto():
    numeros = list(range(1,46))
    resultat = []
    for i in range(5):
        rnd = randrange(46-i)
        resultat.append(numeros[rnd])
        numeros[rnd] = numeros[-1]
    resultat.append(randrange(10)+1)
    return resultat
print("\n---lotto-----------\n")
print(lotto())

print("\n---Decimal-----------\n")

import decimal
a, b = decimal.Decimal('1'),decimal.Decimal('3')
print(type(a/b))
print((a/b))
decimal.getcontext().prec = 3
print((a/b))
print("\n---Decimal-----------\n")
from random import *
from decimal import *

print(random())
print(uniform(1,100))
print(randint(1,100))
print(choice("1234567890abcdefghijklnmopqrstuvwxyz"))
sample_list = ["python", "java", "C++", "random", "spring"]
shuffle(sample_list)
print(sample_list)
print(getcontext())

print("\n---Datetime , Time 모듈-----------\n")

import datetime, time
d = datetime.date.today()
print(d.isoformat())
print(d.ctime())
print(d.strftime("%y/%m/%d"))

print('Now : ', datetime.datetime.day)
print('Today : ', datetime.datetime.today())
print('UTC Now : ', datetime.datetime.utcnow())

# 몇일후 날자짜 구하기
# Start_time = datetime.datetime(2017,12,25,0,0,0) #특정날짜
Start_time = datetime.datetime.today()  #오늘
Offset = datetime.timedelta(days=3)
End_time = Start_time + Offset
print(End_time)

print("\n---도전과제 : 오늘날짜, 시간구하기 -----------\n")

today = datetime.datetime.today()
print(today)

afterday = today + datetime.timedelta(days=100)
print(afterday.strftime("%y/%m/%d"))

week = ["월", '화', '수', '목', '금', '토', '일'];
newyear = (datetime.datetime(2021,2,11).weekday())
print([week[newyear] + "요일"])

