import requests
from bs4 import BeautifulSoup
import re

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

code = "H0000472"

r = requests.get("http://starwars.hankyung.com/cast/?refresh=1&id=ALL&trade=0" ).text
soup = BeautifulSoup(r, "html.parser")
#hotKeys = soup.select("tbody > tr > td ") #td.lft span.crUp
hotKeys = soup.select("tbody > tr:nth-child(1) > td:nth-child(2) > a ")
#contentsList > tr:nth-child(1) > td:nth-child(2) > a
print(hotKeys)