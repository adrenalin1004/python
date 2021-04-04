import pandas as pd

stock_code = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]

stock_code.sort_values(['상장일'], ascending=True)

stock_code = stock_code[['회사명','종목코드']]

stock_code = stock_code.rename(columns={'회사명': 'company', '종목코드': 'code'})

stock_code.code = stock_code.code.map('{:06d}'.format)

company = 'LG화학'
code = stock_code[stock_code.company==company].code.values[0].strip()

df = pd.DataFrame()
for page in range(1, 10):
    url = 'https://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code)
    url = '{url}&page={page}'.format(url=url, page=page)
    print(url)
    df = df.append(pd.read_html(url, header=0)[0], ignore_index=True)

df = df.dropna()

df = df.rename(columns= {'날짜': 'date', '종가' : 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가':'low','거래량':'volume'})

df[['close','diff','open','high','low','volume']] = df[['close','diff','open','high','low','volume']].astype(int)

df['date'] = pd.to_datetime(df['date'])

df = df.sort_values(by=['date'], ascending=True)

df.head()

print(df)
'''
import matplotlib.pyplot as plt
# 필요한 모듈 import 하기 
import plotly
import plotly.graph_objects as go
import plotly.express as px

plt.figure(figsize=(10,4))
plt.plot(df['date'], df['close'])
plt.xlabel('')
plt.ylabel('close')
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off
plt.savefig(company + ".png")
plt.show()
'''