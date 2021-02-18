from _typeshed import OpenTextMode


class Address:
    name = 'Damin'
    addr = "seuoul"
    tel = "02-0002-22020"

print(Address.name, Address.addr, Address.tel)

class MyList:
    def empty(self):
        self.data=[]
    def add(self,x):
        self.data.append(x)
    def getData(self):
        return list(self.data)

my01 = MyList()
my01.empty()
my01.add((list(range(int(1),int(6)))))
print(my01.getData())


class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def aboutPerson(self):
        print("name: "+ self.name + ",age: " + str(self.age))

objectPerson = Person("Dominica", 20)
objectPerson.aboutPerson()

### 연산자 오버로딩

class Num:
    def __init__(self, num):
        self.Num = num
    
    def _add__(self, num):
        self.Num += num

    def __sub__(self, num):
        self.Num -= num
n = Num(100)
print(n.Num)

class MYSU:
    def __init__(self, Su):
        self.Su = Su
    def __lt__(self, Su):
        print("self,Su < other.Su")
    def __gt__(self, Su):
        print("self.Su > other.Su")

a=MYSU(100)
b=MYSU(50)
a>b


print("------------------")

class Dog:
    def sound(self):
        print ("bark")
    
class Cat:
    def sound(self):
        print ("meout")
    
class Chimera(Dog,Cat):
    pass

Chimera().sound()

print("---도전과제  학점계산-----")
class MyScore:
    def __init__(self, kor, eng):
        self.kor = kor
        self.eng = eng
    def getTot(self):
        return (self.kor+self.eng)
    
class MyScore_Sub(MyScore):
    def __init__(self, kor, eng, mat):
        self.mat = mat
        super().__init__(kor, eng)
    def getTot(self):
        return ((super().getTot()+self.mat))

class MyRes(MyScore_Sub):
    def __init__(self, kor, eng, mat, music):
        self.music = music
        super().__init__(kor,eng,mat)
    def getTot(self):
        return (super().getTot()+self.music)
my = MyRes(90,90,90,90)
print(my.getTot())

print('----도전과제 온도계산----')
class Doitch08:
    def __init__(self, temperature = 0):
        self._temperature = temperature
    def to_value(self):
        return (self.temperature * 1.8) +32
    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self, value):
        self._temperature = value
v = Doitch08()
for i in range(10,15):
    v.temperature = i
    print(str(v.to_value()))