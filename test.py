
print('\n------사용자 exception  ---\n')
import sys
import traceback

def my_test(value1, value2):
    print('계산을 시작합니다.')
    result = 0
    try:
        result = value1 + value2
    except:
        print('타입 에러라 계산을 할수 없음')
        raise
    finally:
        print("calc end")
    return result

def calc(list1, list2):
    try:
        print(my_test(list1[0],list2[0]))
        print(my_test(list1[1],list2[1]))
        print(my_test(list1[2],list2[2]))
    except:
        #print("오류가 발생")
        print(traceback.format_exc(sys.exc_info()[2]))
        
if __name__ == "__main__":
    list1 = [100,200,300]
    list2 = [100,200,300]
    calc(list1,list2)

print('\n------도전과제 : 0보다 큰 정수만 입력받고 아니면 exception  ---\n')

class MyException(Exception):
    def __init__(self, message):
        self.message = message

try:
    num1, num2 = eval(input("input num1, num2: "))
    if num2 == 0:
        raise MyException("0으로 나누려 했음")
    result = num1/num2
    print("result is : ", result)
except MyException as e:
    print(e.message)