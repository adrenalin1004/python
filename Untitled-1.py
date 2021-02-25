def sum(a, b):
    result = a + b
    return result
print (sum(1,2))

add = lambda a, b: a+b
print(add(12,2))

mylist = [lambda a, b: a-b, lambda a, b: a*b]
print(mylist[0](2,2))

print ('---------------------')

for i in range(10):
    print(i, end = ' ')

print ('---------------------')

''' 파일 읽고 쓰기 '''

f = open("D:/Python/new.txt", 'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

print ('---------------------')
f = open("D:/Python/new.txt", 'r')
line = f.readline()
print(line)
f.close()


print ('---------------------')

f = open("D:/Python/new.txt", 'a')
for i in range (11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

print ('---------------------')

f = open("D:/Python/new.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line, end="")
f.close()


print ('---------------------')


######### Immutable #########

a = 1
def vartest(a):
    a = a + 1
   # return a
#a = vartest(a)
vartest(a)
print(a)

######### mutable ##########
b = [1,2,3]
def vartest2(b):
    b = b.append(4)
vartest2(b)
print(b)

######### 클래스 ##########

result1 = 0
result2 = 0

def add1(num) :
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 -= num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(4))

""" 클래스정의 """
class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))

print('----------------')

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
class MoreCal(FourCal):
    def pow(self):
        if self.second == 0 :
            return 0
        else :
            return  self.first * self.second
     
a = MoreCal(10,20)

print(a.pow())
#a.setdata(1,2)
#print(a.first)
#print(a.second)
#print(a.add())
