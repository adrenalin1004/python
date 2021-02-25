'''
num = int(input("입력해주세요 : "))
if num >=1 and num <= 10:
    print('Great')
else:
    print('Wrong~')
'''
print('-if문---------------------')
score = 99
#score = int(input("input 점수: "))
if score >= 90 :
    print("A")
elif score >= 80 and score < 90 :
    print ("B")
elif score >=70 and score < 80 :
    print("C")
else:
    print("D")

print('-while-For문-------------------')
i = 5
while i <=10:
    print (i)
    i+=1

m_dict = {'X':1, "Y":2, "Z":3}
for key in m_dict:
    print(key, '+', m_dict[key])
print('--range--------------------')
r = list(range(10))
r1 = list(range(2,8))
r2 = list(range(2,20,3))
print(r)
print(r1)
print(r2)
print('--Enumerate--------------------')
for index, value in enumerate(['apple','watermelon','melon','banana']):
    print(index,value)

my_str = ['apple','watermelon','melon','banana']
print(list(enumerate(my_str)))

fruit = ['apple','watermelon','melon','banana']
for i in enumerate(fruit,100):
    print(i)

print('--continue,break---------------')
pwList = ["123","345"]
valid = False
count = 3
while count > 0:
    res = input("비번 입력 > ")
    for eachPasswd in pwList:
        if res == eachPasswd:
            valid = True
            break
    if not valid:
        print("invalid input")
        count -= 1
        continue
    else:
        break

print('--도전과제---------------')

while True:
    res = input("enter word: ")
    if res == 'quit':
        break
    if len(res) < 5:
        print("Too Small")
    else :
        print(res)
    continue