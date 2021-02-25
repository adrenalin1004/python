def Hello():
    return 3, "ABC"
n,s = Hello()
print(n,s)
print("-------------------------")

def addsub(x,y):
    return x+y, x-y

h,s = addsub(10,5)
print("10+5 = %s" %h)
print("10-5 = %s" %s)

def repeat_msg(msg,repeat=3):
    for i in range(repeat):
        print(msg)
repeat_msg("Hello")
repeat_msg("Hi", repeat=5)
print("-------------------------")

def add(a, b):
    print("ADDing %d + %d" %(a,b))
    return a+b

def subtract(a,b):
    print("SUBStracting %d - %d" %(a,b))
    return a-b

def multiply(a,b):
    print("Multiplying %d * %d" % (a,b))
    return a*b

def divide(a,b):
    print("Dividing %d / %d" % (a,b))
    return a/b

def Choose_menu():
    print("원하는 연산을 고르세요~")
    print("add, sub, mul, div, quit")
    return input("당신의 선택은 : ")