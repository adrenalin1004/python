# Exception
try :
    10/0
except ZeroDivisionError as e:
    print(e)

L = [1,2,3]
try:
    num=L[4]
except IndexError:
    print("indexError")
else:
    print('Keep calm and go ahead')

try:
    print('try - 시작')
    #예외발생
    #a = int('string')
    print('try-종료')
except (ZeroDivisionError, IOError):
    print('0으로 나눈 파일이 존재하지 않음')
else:
    print('else 왔어요')
finally:
    print('finally')

import sys
try:
    10/0
except:
    print(sys.exc_info())

import traceback
def f1(a,b):
    return f2(a) + f2(b)
def f2(x):
    return 1.0/x

try:
    f1(1.0, 0.0)
except:
    traceback.print_exc()

def excption_test(value1, value2):
    print('계산을 시작합니다.')
    result = 0
    try:
        result = value1 + value2
    except:
        print('계산을 할 수 없습니다.')
    finally:
        print('계산을 종료합니다.')
    return result

if __name__ == "__main__":
    print(excption_test(100,200))
    print(excption_test(100,"200"))

print('\n------assert문 이용한 ---\n')

def check_assert():
    a = 3
    b = 2
    assert a < b, "'a'가 b보다 작다"
    print("a=" + str(a) + "b=" + str(b))

try:
    check_assert()
except Exception as e:
    print("Exception: check_assert", e)

print('\n------Unitest를 이용한 ---\n')

import unittest
class MyTest(unittest.TestCase):
    def test1(self):
        print("test1")
    def test2(self):
        print("test2")
        assert True == True

TS = unittest.TestSuite()
TS.addTest(MyTest("test1"))
TS.addTest(MyTest("test2"))
TS2 = unittest.makeSuite(MyTest, "test")

#unittest.main()

print('\n------assert 메소드 사용을 통한 Unitest를 이용 ---\n')
#import unittest
class TestM(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('python'.upper(), 'PYTHON')
    def test_isupper(self):
        self.assertTrue('PYTHON'.isupper())
        self.assertFalse('PYTHON'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
if __name__ == '__main__':
    unittest.main()

print('\n------사용자 exception  ---\n')
# import sys
# import traceback

# def my_test(value1, value2):
#     print('계산을 시작합니다.')
#     result = 0
#     try:
#         result = value1 + value2
#     except:
#         print('타입 에러라 계산을 할수 없음')
#         raise
#     finally:
#         print("calc end")
#     return result

# def calc(list1, list2):
#     try:
#         print(my_test(list1[0],list2[0]))
#         print(my_test(list1[1],list2[1]))
#         print(my_test(list1[2],list2[2]))
#     except:
#         #print("오류가 발생")
#         print(traceback.format_exc(sys.exc_info()[2]))
        
# if __name__ == "__main__":
#     list1 = [100,200,300]
#     list2 = [100,200,"300"]
#     calc(list1,list2)

# print('\n------도전과제 : 0보다 큰 정수만 입력받고 아니면 exception  ---\n')

# class MyException(Exception):
#     def __init__(self, message):
#         self.message = message

# try:
#     num1, num2 = eval(input("input num1, num2: "))
#     if num2 == 0:
#         raise MyException("0으로 나누려 했음")
#     result = num1/num2
#     print("result is : ", result)
# except MyException as e:
#     print(e.message)