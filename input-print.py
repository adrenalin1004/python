import re
'''
print('표준입력과 출력')

print("a","b",sep=":-)")

str = input("이름이 뭐니: ")
print("ur nicname : {0}".format(str))
print('-------------------')

a = int(input("input 숫자 a : "))
b = int(input("input 숫자 b : "))
sum  = a+b
print(sum)

val = tuple(input("input 튜플 val: "))
print(val)

print('---정규식 re모듈 --특정한규칙을가진문자열집합--------------')


m_str = 'matches the start of a string.'
m = re.match('[a-z]+',m_str);
r = re.search('[a-z]+',m_str);
print(m)
print(r)

print('----------')

s = 'Payday is 25th of every month'
p = re.search('(\d{2})',s).group()
print(p)
'''
print('--re모듈--------')
re=re.findall("app\w*","application orange apple banana")

print(re)

print('--re.sub--------')

import re
re1= re.sub('[:,|\s]','---','one:two tree|four',2)
print(re1)

print('--re.compile--------')

import re
telcheck=re.compile(r'(\d{2,3})-(\d{3,4})-(\d{4})')
print(bool(telcheck.match('02-134-4566')))
print(bool(telcheck.match('02-가123-3456')))
print(bool(telcheck.match('3402-123-4455')))
print(bool(telcheck.match('032-123-4567')))
print(telcheck.match('032-124-4567'))



print('--re.compile groups--------')
phone=re.compile(r'(\d{3})-(\d{3,4})-(\d{4})')
m=phone.match('010-123-4577')
print(m.groups())
print(m.group())
print(m.group(2,3))

print(m.start())
print(m.end())
print(m.start(2))
print(m.end(2))
print(m.string[m.start(2):m.end(3)])

print('--findall()--------')
import re
s = 'matches the start of a string'
result = re.findall('[a-z]+',s)
print(result)

p = re.compile('\d+')
res = p.findall('12AM, 24 allday, 10 pm')
print(res)

print('★★★도전과제★★★')
my_str = "My mobile phone number is 010-134-2040"
import re
MPattern = re.compile('(\d{3})-(\d{3})-(\d{4})$')
Mres = re.search(MPattern,my_str).groups()
print(Mres)
MPattern02 = re.compile('[-,|\s]')
print(re.sub(MPattern02, ':', my_str,5))

