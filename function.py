def add(a,b):
    print("더하기 %d + %d" %(a,b))
    return a+b

def subtract(a,b):
    print("빼기 %d - %d" %(a,b))
    return (a-b)

def multiply(a,b):
    print("곱하기 %d * %d" %(a,b))
    return a*b

def divide(a,b):
    print("나누기 %d / %d" %(a,b))
    return a/b

def Choose_menu():
    print("원하는 메뉴를 고르세요 ")
    print("add, sub, mul, div, quit")
    return input("당신의 선택은 : ")

menu = {'add':add , 'sub':subtract, 'mul':multiply, 'div':divide}
choice = Choose_menu()

while choice != quit:
    if menu.get(choice):
        x = input("첫번째 숫자를 입력하세요: ")
        y = input("두번째 숫자를 입력하세요: ")
        print(menu[choice](int(x),int(y)))
        choice = Choose_menu
        break
    break

print('----------------------------------------------')
###### lambda calculus #########

def even(x):
    return (x%2 == 0)
lst = range(10)
print(list(filter(even,lst)))
print("\n lambda 표현 : (list(filter(lambda x: x%2 == 0, range(10)))")
print(list(filter(lambda x: x%2 == 0, range(10))))
print("\n reduce ")
from functools import reduce
print(reduce(lambda x,y:x+y , range(1,11)))

def hap(a,b,c):
    return a+b+c
print(hap(10,20,30))

hap01 = lambda a,b,c : a+b+c
print(hap01(10,20,30))

def info(x):
    return x+2
a = info(1)
print(a)

f=lambda x : x+2
a=f(1)
print(a)

min = (lambda x, y: x if x <y else y)
print(min(100,200))

print("---도전과제, 화씨를 섭씨로 변환 ---")

def fahrenheit(t):
    return t*9/5+32

for t in (22.6,25.8,27.3,29.8):
    print(t, "C : ", fahrenheit(t), "F")

print(fahrenheit(100))