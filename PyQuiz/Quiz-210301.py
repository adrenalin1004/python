##########################################
#### 초보자를 위한 파이썬 300제         ####
#### https://wikidocs.net/book/922    ####
##########################################

# Start of Code
""" 
#1. 화면에 Hello World 문자열을 출력하세요
print('Hello World')

#2. 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)
print('Mary\'s cosmetics')
print("Mary's cosmetics")

#3. 신씨가 소리질렀다. "도둑이야". 출력
print('신씨가 소리질렀다. \"도둑이야\".')
print('신씨가 소리질렀다. "도둑이야".')

#4. 화면에 "C:\Windows"를 출력하세요.
print('"C:\windows"')

#5. \t와 \n의 역할을 설명, \n 줄바꿈, \t 탭
print("안녕하세요.\n만나서\t\t반갑습니다.")

#6. print 함수에 두 개의 단어를 입력한 예제
print("오늘은", "일요일")

#7. naver;kakao;sk;samsung 출력
print("naver","kakao","sk;samsung", sep=";")

#8. naver/kakao/sk/samsung 출력
print("naver","kakao","sk","samsung", sep="/")

#9. print("first");print("second") 수정하여 줄바꿈이 없이 출력, 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용
print("first",end=""); print("second")

#10. 5/3의 결과를 화면에 출력
print(5/3)

#11. 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력
Sam = 50000
print(Sam*10)

#12.  변수를 사용해서 시가총액, 현재가, PER 등을 바인딩
siga = 2980000000000
Cvalue = 50000
PER = 15.79
print("시가총액= %s, 현재가=%s, PER=%s" %(siga,Cvalue,PER))

#13. s = "hello",t = "python" 두 변수를 이용하여 아래와 같이 출력
s = "hello"
t = "python"
print(s+"!"+" "+t)

#14. 2 + 2 * 3 코드의 실행 결과 => 8
print(2+2*3)

#15. type() 함수는 데이터 타입을 판별 a = "132"
a = "132"
print(type(a))

#16. 문자열 '720'를 정수형으로 변환
num_str = "720"
num_int = int(num_str)
print(num_int,type(num_int))

#17. 정수 100을 문자열 '100'으로 변환
num = 100
result = str(num)
print(result, type(result))

#18. 문자열 "15.79"를 실수(float) 타입으로 변환
A = "15.79"
B = float(A)
print(B, type(B))

#19. year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력
year = "2020"
int_year = int(year)
print(int_year, int_year-1, int_year-2)

#20. 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산
aircon = 48584*36
print(aircon)

#21. letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력
letters = 'python'
print(letters[0],letters[2])

#22. 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력
license_plate = "24가 2210"
print(license_plate[-4:])

#23. 문자열에서 '홀' 만 출력
string = "홀짝홀짝홀짝"
print(string[::2])

#24. 문자열을 거꾸로 뒤집어 출력
string = "PYTHON"
print(string[::-1])

#25. 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력
phone_number = "010-1111-2222"
re_num = phone_number.replace("-", " ")
print(re_num)

#26. 전화번호를 아래와 같이 모두 붙여 출력
phone_number = "010-1111-2222"
re_num = phone_number.replace("-", "")
print(re_num)

#27. url 에 저장된 웹 페이지 주소에서 도메인을 출력
url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

#28. 코드의 실행 결과를 예상 => 문자열은 수정할 수 없음.
lang = 'python'
#lang[0] ='P' #문자열이 할당(assignment) 메서드를 지원하지 않음
print(lang)

#29. 문자열에서 소문자 'a'를 대문자 'A'로 변경
string = 'abcdfe2a354a32a'
result = string.replace('a','A')
print(result)

#30. 코드의 실행 결과를 예상 => abcd
string = 'abcd'
string.replace('b', 'B') #문자열은 변경할 수 없는 자료형
print(string)

#31. 문자열 합치기, 아래 코드의 실행 결과를 예상
a = '3'
b = '4'
print(a+b) #34

#32. 문자열 곱하기, 아래 코드의 실행 결과
print("Hi"*3)

#33. 문자열 곱하기, 화면에 '-'를 80개 출력
print('-'*80)

#34. 문자열 곱하기, 변수에 문자열 더하기와 문자열 곱하기를 사용
t1 = 'python'
t2 = 'java'
print((t1+' '+t2+' ')*4)

#35. 문자열 출력, 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" %(name1,age1))
print("이름: %s 나이: %d" %(name2,age2))

#36. 문자열 출력, 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}" .format(name1,age1))
print("이름: {} 나이: {}" .format(name2,age2))

#37. 문자열 출력, 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}" )
print(f"이름: {name2} 나이: {age2}" )

#38. 컴마 제거하기, 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환
상장주식수 = "5,969,782,550"
result = int(상장주식수.replace(',',''))
print(result, type(result))

#39.문자열 슬라이싱, 문자열에서 '2020/03'만 출력
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

#40. strip 메서드, 문자열의 좌우의 공백이 있을 때 이를 제거 (문자열에서 strip( ) 메서드를 사용하면 좌우의 공백을 제거)
data = "   삼성전자    "
#공백제거 = data.replace("   ",'')
공백제거 = data.strip()
print(공백제거)

#41. upper 메서드, 대문자 BTC_KRW로 변경
ticker = "btc_krw"
print(ticker.upper())

#42. lower 메서드, 소문자 btc_krw로 변경
ticker = "BTC_KRW"
ticker1 = ticker.lower()
print(ticker1)

#43. capitalize 메서드, 문자열 'hello'가 있을 때 이를 'Hello'로 변경
A = 'hello'
print(A.capitalize())

#44. endswith 메서드, 파일 이름이 'xlsx'로 끝나는지 확인
file_name = "보고서.xlsx"
print(file_name.endswith('.xlsx'))

#45. endswith 메서드, 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx","xls")))

#46. startswith 메서드, 파일 이름이 '2020'로 시작하는지 확인
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

#47. split 메서드, 공백을 기준으로 문자열을 나눠보세요
a = "hello world"
print(a.split())

#48. split 메서드, btc와 krw로 나눠보세요.
ticker = "btc_krw"
print(ticker.split("_"))

#49. split 메서드, 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
date = "2020-05-01"
print(date.split("-"))

#50. rstrip 메서드, 문자열의 오른쪽에 공백이 있을 때 이를 제거
data = "039490     "
print(data.rstrip())

#51. 리스트 생성, 영화 제목을 movie_rank 이름의 리스트에 저장
mov = ['닥터 스트레인지','스플릿','럭키']
print(mov)

#52.리스트에 원소 추가, movie_rank 리스트에 "배트맨"을 추가
mov.append('배트맨')
print(mov)

#53. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가
mov.insert(1,"슈퍼맨")
print(mov)

#54. 리스트에서 '럭키'를 삭제
del mov[3]
print(mov)

#55.  '스플릿' 과 '배트맨'을 를 삭제
del mov[2]
del mov[2]
print(mov)

#56. lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1+lang2
print(langs)

#57. 리스트에서 최댓값과 최솟값을 출력
nums = [1, 2, 3, 4, 5, 6, 7]
print("min: ", min(nums), "max: ", max(nums))

#58. 리스트의 합을 출력
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#59. 리스트에 저장된 데이터의 개수를 화면에 구하하라.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

#60. 리스트의 평균
nums = [1, 2, 3, 4, 5]
average = sum(nums)/len(nums)
print(average)

#61. 날짜 정보를 제외하고 가격 정보만을 출력
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#62. 슬라이싱을 사용해서 홀수만 출력
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#63. 슬라이싱을 사용해서 짝수만 출력
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

#64. 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#65. interest 리스트를 사용하여 아래와 같이 화면에 출력
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

#66. interest 리스트를 사용하여 아래와 같이 화면에 출력
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

#67. join 메서드, interest 리스트를 사용하여 아래와 같이 화면에 출력
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

#68. join 메서드, interest 리스트를 사용하여 아래와 같이 화면에 출력
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

#69. 문자열 split 메서드 interest 이름의 리스트로 분리 저장
string = "삼성전자/LG전자/Naver"
print(string.split("/"))

#70. 리스트에 있는 값을 오름차순으로 정렬
data = [2, 4, 3, 1, 5, 10, 9]
#data.sort()
sorted(data)
print(data)

#71. my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()
print(type(my_variable))

#72. 영화 제목을 movie_rank 이름의 튜플에 저장
mv = ("닥터스트레인지","스필릿","럭키")
print(mv, type(mv))

#73. 숫자 1 이 저장된 튜플을 생성, 하나의 데이터가 저장되는 경우, 아래와 같이 쉼표를 입력해만 튜플
#tup = (1) #정수 int
tup = (1,) #튜플 tuple
print(tup, type(tup))

#74. 오류 원인을 찾아라. 
#t = (1, 2, 3)
#t[0] = 'a'    #튜풀은 data(element값)을 변경 할 수 없다.

#75. t가 바인딩하는 데이터 타입은 무엇
t = 1, 2, 3, 4
print(type(t)) #튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호 없이도 동작

#76. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)

#77. 튜플을 리스트로 변환
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest_l=list(interest)
print(list(interest_l), type(interest_l))

#78. 리스트를 튜플로 변경
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)
print(data, type(data))

#79. 튜플 언팩킹
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

#80. 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성
data = tuple(range(2,100,2))
print(data)

#81. 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
#valid_score = scores[2:]
*valid_score, _, _=scores
print(valid_score)

#82. 우측 8개의 값을 valid_score 변수에 바인딩
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *v_scores=scores
print(v_scores)

#83. 가운데 있는 8개의 값을 valid_score 변수에 바인딩
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *v_scores, b = scores
print(v_scores)
print(a,b)

#84. temp 이름의 비어있는 딕셔너리
temp = {}
print(temp)

#85. 아이스크림 이름과 희망 가격을 딕셔너리로 구성
values = {"메로나":1000, "폴라포":1200, "빵빠레":1800}
print(values)

#86. 85번 딕셔너리에 가격추가
values["죠스바"] = 1200
values["월드콘"] = 1500
print(values)

#87. 메로나 가격을 출력
print("메로나 가격 : ", values["메로나"])

#88. 메로나 가격 1300으로 수정
values["메로나"] = 1300
print(values)

#89. 메로나 삭제
del values["메로나"]
print(values)

#90. 에러 발생 원인은
# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바'] # 딕셔너리에 없는 key를 사용해서

#91. 리스트를 딕셔너리의 값으로 저장
inventory = {"메로나" : [300, 20], "비비빅" : [400, 3], "죠스바" : [250,100]}
print(inventory, type(inventory))

#92. 메로나의 가격을 화면에 출력
print(inventory["메로나"][0],"원")

#93. 메로나의 재고를 화면에 출력
print(inventory["메로나"][1],"개")

#94. 데이터 추가
inventory["월드콘"] =(500,7)
print(inventory)

#95. key값으로 구성된 리스트 생성
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream.keys()))

#96. values값으로 구성된 리스트 생성
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream.values()))

#97.아이스크림 판매 금액의 총합을 출력
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(sum(icecream.values()))

#98. new_product을 icecream 딕셔너리에 추가
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

#99. 두 개의 튜플을 하나의 딕셔너리로 변환
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys,vals))
print(result)

#100.  두 개의 리스트를 close_table 이름의 딕셔너리로 생성
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))
print(close_table)

#101.  True 혹은 False를 갖는 데이터 타입은 무엇
print(bool, type(True))

#102. 출력 결과를 예상
print(3==5) #False

#103. 출력 결과를 예상
print(3 < 5) #True

#104. 결과를 예상
x = 4
print(1 < x < 5) # True

#105.결과를 예상
print ((3 == 3) and (4 != 3)) #True

#106. 에러가 발생하는 원인
#print(3 => 4) #연산자가 아님. print(3 <= 4) 실행됨

#107. 결과를 예상
if 4 < 3:
    print("Hello World") # 출력없음

#108. 출력 결과를 예상하라
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.") # 출력됨

#109. 출력 결과를 예상하라
if True :
    print ("1") # 출력됨
    print ("2") # 출력됨
else :
    print("3")
print("4")  # 출력됨

#110. 출력 결과를 예상하라
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3") # 출력됨
else :
    print("4")
print("5") # 출력됨

#111. 사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.
A = input("#111  안녕하세요를 입력하세요.")
print(A*2)

#112. 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
A = int(input("#112 숫자를 입력하세요.: "))
print(A+10)

#113. 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
A = int(input("#113 숫자를 입력하세요: "))
if A % 2 == 0 :
    B = "짝수"
else :
    B = "홀수"
print(B)

#114. 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라. 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.
A = int(input("#114 숫자를 입력하세요: "))
B = A+20
if B > 255:
    print(255)
else:
    print(B)

#115. 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 출력 값의 범위는 0~255이다. 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.
num = input("#115 숫자를 입력: ")
result = int(num) - 20
if result < 0:
    print(0)
elif result > 255:
    print(255)
else :
    print(result)

#116. 사용자로부터 입력 받은 시간이 정각인지 판별
time = input("#116 시간을 입력: ")
if time[-2:] =="00" :
    print("정각입니다.")
else:
    print("정각이 아님")

#117. 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
fruit = ["사과", "포도", "홍시"]
user = input("#117 과일입력 : ")
if user in fruit:
    print("정답")
else:
    print("오답")

#118. 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
stock = input("#118 종목을 입력: ")
if stock in warn_investment_list:
    print("투자경고 종목")
else:
    print("투자경고 종목아님")

#119. 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("#119 계절을 입력: ")
if user in fruit:
    print("정답")
else :
    print("오답")

#120 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("#120 과일을 입력: ")
if user in fruit.values():
    print("정답")
else:
    print("오답")

#121 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력
A = input("#121 문자입력 : ")
if A.islower() :
    print(A.upper())
else:
    print(A.lower())

#122 사용자로부터 score를 입력받아 학점을 출력
score = int(input("#122 학점을 입력: "))
if 81 <= score <= 100 :
    print("A학점")
elif 61 <= score <= 80 :
    print("B학점")
elif 41 <= score <= 60 :
    print("C학점")
elif 21 <= score <= 40 :
    print("D학점")
else :
    print("E학점")

#123 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성
환율 = {"달러": 1167,
        "엔": 1.096,
        "유로": 1268,
        "위안": 171}
price = input("#123 입금액: ")

num, currency = price.split()
print(float(num) * 환율[currency], "원")

#124 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력
A = int(input("#124 첫번째 숫자입력 : "))
B = int(input("#124 두번째 숫자입력 : "))
C = int(input("#124 세번째 숫자입력 : "))

if A > B and A > C :
    print(A)
elif B > C and B > A:
    print(B)
else:
    print(C)

#125 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성
통신사 = { "011" : "SKT",
           "016" : "KT",
           "019" : "LGU",
           "010" : "통합"}

phone_number = input("#125 전화번호를 입력 : ")
tong,num1,num2 = phone_number.split("-")
print(통신사[tong])

#126 사용자로 부터 5자리 우편번호를 입력받고 구를 판별
A = (input("#126 우편번호 숫자5개(0~9)입력 : "))
B = A[:3]
if A[:3] in ["010","011","012"] :
    print("도봉구")
elif B in ["013","014","015"] :
    print("강북구")
else :
    print("노원구")

#127 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성
A = input("#127 주민번호를 입력(xxx-xxx): ")
B = A.split("-")[1]
if B[0] == "1" or B[0] == "3":
    print("남자입니다. %s" %B[0])
else :
    print("여자입니다.%s" %B[0])
  
#128 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성
A = input("#128 주민번호를 입력(xxx-xxx): ")
B = A.split("-")[1]
if B[1:3] in ["00","01","02","03","04","05","06","07","08"] :
    print("출생지 : 서울, %s" %B[1:3])
elif B[1:3] in ["09","10","11","12"] :
    print("출생지 : 부산, %s" %B[1:3])
else : 
    print("출생지 : 알수없음, %s" %B[1:3])

#129 주민등록번호가 유효한지를 출력하는 프로그램을 작성
A = input("#128 주민번호를 입력(xxx-xxx): ")
B = A.split("-")
C = int(B[0][:1])*2 + int(B[0][1:2])*3 + int(B[0][2:3])*4 + int(B[0][3:4])*5 + int(B[0][4:5])*6 + int(B[0][5:6])*7 
D = int(B[1][:1])*8 + int(B[1][1:2])*9 + int(B[1][2:3])*2 + int(B[1][3:4])*3 + int(B[1][4:5])*4 + int(B[1][5:6])*5
sum1 = C+D
result = 11 - (sum1 % 11)
if result == int(B[1][6:]):
    print("유효한 주민번호임")
else :
    print("가짜 주민번호임")
    
#130 최고가와 최저가의 차이
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
print(btc)
opening_price = btc['opening_price']
min_price = btc['min_price']
max_price = btc['max_price']
valuation = int(max_price) - int(min_price)
result = int(opening_price) + valuation
print(result, max_price)
if result > int(max_price):
    print("상승장")
else:
    print("하락장")

#131 for문의 실행결과를 예측
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수) #사과, 귤, 수박

#132 for문의 실행결과를 예측하라.
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####132") ####

#133 다음 for 문과 동일한 기능을 수행하는 코드를 작성하세요.
for 변수 in ["A", "B", "C"]:
  print(변수)

#134 for문을 풀어서 동일한 동작을하는 코드를 작성하라.
for 변수 in ["A", "B", "C"]:
  print("출력:", 변수)

#135 for문을 풀어서 동일한 동작을 하는 코드를 작성하라.
for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)

#136 다음 코드를 for문으로 작성하라.
# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)
for 변수 in [10, 20, 30]:
    print("#136", 변수)

#137 다음 코드를 for문으로 작성하라.
# print(10)
# print(20)
# print(30)
for i in [10,20,30]:
    print("#136", i)

#138 다음 코드를 for문으로 작성하라.
# print(10)
# print("-------")
# print(20)
# print("-------")
# print(30)
# print("-------")
for i in [10, 20, 30]:
    print(i)
    print("#138 --------")

#139 다음 코드를 for문으로 작성하라.
# print("++++")
# print(10)
# print(20)
# print(30)
print("#139 +++++")
for i in [10,20,30]:
    print(i)

#140 다음 코드를 for문으로 작성하라.
# print("-------")
# print("-------")
# print("-------")
# print("-------")

for i in [1,2,3,4] :
    print("#140 --------")

#141 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라. 단 부가세는 10원으로 가정한다.
리스트 = [100, 200, 300]
for i in 리스트 :
    i=i+10
    print(i)

#142 for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.
리스트 = ["김밥", "라면", "튀김"]
for i in 리스트 :
    print("#142 오늘의 메뉴: ", i)

#143 저장된 문자열의 길이를 다음과 같이 출력하라.
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
    i = len(i)
    print(i)

#144 동물 이름과 글자수를 다음과 같이 출력
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i, len(i))

#145 for문을 사용해서 동물 이름의 첫 글자만 출력
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i[0])

#146 for문을 사용해서 다음과 같이 출력
리스트 = [1, 2, 3]
for i in 리스트:
    print("#146 3 x", i)

#147 for문을 사용해서 다음과 같이 출력
리스트 = [1, 2, 3]
for i in 리스트:
    result = (3*i)
    print("#147 3 x %s = %s" %(i, result))
    print("3 x {} = {}".format(i, 3*i))

#148 for문을 사용해서 다음과 같이 출력
리스트 = ["가", "나", "다", "라"]
for i in 리스트:
    if i != "가":
        print(i)

#149 for문을 사용해서 다음과 같이 출력
리스트 = ["가", "나", "다", "라"]
리스트1 = 리스트[::2]
for i in 리스트[::2]:
    print(i)

#150 for문을 사용해서 다음과 같이 출력
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::-1]:
    print(i)

#151 for문을 사용해서 리스트의 음수를 출력
리스트 = [3, -20, -3, 44]
for i in 리스트:
    if i < 0 :
        print(i)

#152 for문을 사용해서 3의 배수만을 출력
리스트 = [3, 100, 23, 44]
for i in 리스트:
    if i%3 == 0 :
        print(i)

#153 리스트에서 20 보다 작은 3의 배수를 출력
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
    if i < 20 and i % 3 == 0 :
        print(i)

#154 리스트에서 세 글자 이상의 문자를 화면에 출력
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트 :
    if len(i) > 3 :
        print(i)

#155 리스트에서 대문자만 화면에 출력
리스트 = ["A", "b", "c", "D"]
for i in 리스트 :
    if i.isupper() :
        print(i)

#156 리스트에서 소문자만 화면에 출력
리스트 = ["A", "b", "c", "D"]
for i in 리스트 :
    if i.isupper() == False :
        print(i)

#157 이름의 첫 글자를 대문자로 변경해서 출력
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i[0].upper()+i[1:])

#158 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. 
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in 리스트:
   #i[0] = 리스트.split(".")
    print(i.split(".")[0])

#159 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    if i.split(".")[1] == "h":
        print(i)


#160 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트 :
    if i.split(".")[1] == "h" or i.split(".")[1] == "c"   :
        print(i)

#161 for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성
i == 0
for i in range(100) :
    print(i)

#162 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력
for wc in range(2002,2051,4):
    print(wc)

#163 1부터 30까지의 숫자 중 3의 배수를 출력
for i in range(3,31,3):
    print(i)

#164 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력
for i in range(99, 0, -1):
    print(i)

#165 for문을 사용해서 0.0 와 같이 출력
for i in range(10):
    print(i/10)

#166 구구단 3단을 출력
for i in range(1,10):
    print("3x%s = %s" %(i, i*3))

#167 구구단 3단을 출력하라. 단 홀수 번째만 출력
for i in range(1,10):
    if i % 2 != 0:
        print("3x%s = %s" %(i, 3*i))

#168 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성
sum = 0
for i in range(1,11):
    sum += i
print(sum)

#169 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성
sum = 0
for i in range(1,11):
    if i % 2 != 0:
        sum += i
print(sum)

#170 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성
sum = 1
for i in range(1,11):
    sum *= i
print(sum)

#171 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

#172 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(i, price_list[i])

price_list = [32100, 32150, 32000, 32500]
for i, data in enumerate(price_list):
    print(i, data)

#173 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)) :
    print(3-i, price_list[i])

#174 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     if i > 0 :
#         print("1"+str(i)+"0", price_list[i])
for i in range(1, 4):
    print(90 + 10 * i, price_list[i])

#175 my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]

for i in range(len(my_list)-1):
    print(my_list[i], my_list[i+1])

#176 리스트를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라", "마"]

for i in range(len(my_list)-2) :
    print(my_list[i], my_list[i+1], my_list[i+2])

#177 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]
# for i in range(1):
#     print(my_list[3], my_list[2])
#     print(my_list[2], my_list[1])
#     print(my_list[1], my_list[0])
for i in range(len(my_list)-1): #4
    print(my_list[3-i], my_list[2-i])

#178 리스트에는 네 개의 정수가 저장되어 있다. 각각의 데이터에 대해서 자신과 우측값과의 차분값을 화면에 출력하라.
my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1):
    print(my_list[i+1]-my_list[i])

#179 리스트에는 6일 간의 종가 데이터가 저장되어 있다. 종가 데이터의 3일 이동 평균을 계산하고 이를 화면에 출력하라.
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(len(my_list)-2):
    print((my_list[i]+my_list[i+1]+my_list[i+2])/3)

#180 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):
    #print(low_prices[i], high_prices[i])
    #volatility = (high_prices[i]-low_prices[i])
    volatility.append(high_prices[i] - low_prices[i])
    print(volatility)

#181 하나의 행을 하나의 리스트로, 총 3개의 리스트를 갖는 이차원 리스트 apart를 정의하라.
APT = [["101호","102호"],["201호","202호"],["301호","302호"]]
print(APT)

#182 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의하라.
stock = [["시가",100,200,300],["종가",80,210,330]]
print(stock)

#183 stock 이름의 딕셔너리로 표현하라
stock = {"시가": [100,200,300], "종가":[80,210,330]}
print(stock)

#184 stock 이라는 이름의 딕셔너리로 표현하라, 날짜를 key로 저장
stock = {"10/10":[80,110,70,90], "10/11":[210,230,190,200] }
print(stock)

#185 리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")

#186 리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for row in i:
        print(row)

#187 리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for col in i[::-1]:
        print(col)

#188 리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for col in i :
        print(col,"호" , "\n ------")

#189 리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for col in i :
        print(col)
    print("---------")

#190 리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for col in i :
        print(col)
print("---------")

#191 수수료를 0.014 %로 가정할 때, 각 가격에 수수료를 포함한 가격을 한라인에 하나씩 출력하라.
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data:
    for col in i:
        print(col+(col*0.014/100))

#192 191번의 출력 결과에 행단위로 "----" 구분자를 추가하라.
for i in data:
    for col in i:
        print(col+(col*0.014/100))
    print("-------------")

#193. 192 번 문제의 결괏값을 result 이름의 리스트에 1차원 배열로 저장하라.
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for i in data:
    for col in i:
        result.append(col+(col*0.014/100))
print(i)
print(result)

#194. 191번 문제의 결괏값을 result 이름의 리스트에 2차원 배열로 저장하라. 저장 포맷은 아래와 같다. 각 행에 대한 데이터끼리 리스트에 저장되어야 한다.
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data:
    result = []
    for col in i :
        result.append(col+(col*0.014/100))
    print(result)

#195. ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 화면에 종가데이터를 출력하라.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    print(i[3])

#196. ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 150원보다 큰경우에만 종가를 출력하라.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:] :
    if i[3] > 150:
      print(i[3])

#197. 종가가 시가 보다 크거나 같은 경우에만 종가를 출력하라.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:] :
    if i[3] >= i[0] :
        print(i[3])
 
""" # End of Code
#198. ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 고가와 저가의 차이를 변동폭으로 정의할 때 변동폭을 volatility 이름의 리스트에 저장하라.
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = []
#for i in ohlc[1:] :
    #for col in i:
#    volatility.append(i[1]-i[2])
#print(volatility)

#199. 종가가 시가보다 높은 날의 변동성 (고가 - 저가)을 화면에 출력하라
for i in ohlc[1:] :
    if i[3] > i[0]:
       volatility.append(i[1]-i[2])
       print("#199 : ", volatility)

#200. 시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산하라.
val = 0
for i in ohlc[1:] :
    #val = i[3] - i[0]
    val += (i[3] - i[0])
print("#200 : ",val)

#201. "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
def print_coin():
    print("#201: 비트코인")

#202. 201번에서 정의한 함수를 호출하라.
print_coin()

#203. 201번에서 정의한 print_coin 함수를 100번호출하라.
for i in range(10) :
    print_coin()

#204. "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
def print_coins():
    for i in range(10) :
        print("204: 비트코인")

#205. 아래의 에러가 발생하는 이유에 대해 설명하라.
#hello()
def hello():
    print("Hi")

#206. 아래 코드의 실행 결과를 예측하라.
def message() :
    print("A")
    print("B")

message() #A, B
print("C") # C
message() #A, B

#207. 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
print("#207--------------------------------")
print("A")      #A
def message() :
    print("B")
print("C") #C
message()  #B

#208. 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
print("#208--------------------------------")
print("A")     #A
def message1() :
    print("B")
print("C")     #c
def message2() :
    print("D")
message1()     #B
print("E")     #E
message2()     #D

#209. 아래 코드의 실행 결과를 예측하라.
print("#209--------------------------------")
def message1():
    print("A")
def message2():
    print("B")
    message1()
message2()      #B, A

#210. 아래 코드의 실행 결과를 예측하라.
print("#210--------------------------------")
def message1():
    print("A")
def message2():
    print("B")
def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()
message3() #BCBCBC A

#211. 함수의 호출 결과를 예측하라.
print("#211--------------------------------")
def 함수(문자열) :
    print(문자열)
함수("안녕") #안녕
함수("Hi")   #Hi

#212. 함수의 호출 결과를 예측하라.
print("#212--------------------------------")
def 함수(a, b) :
    print(a + b)
함수(3, 4) #7
함수(7, 8) #15

#213. 아래와 같은 에러가 발생하는 원인을 설명하라.
def 함수(문자열) :
    print(문자열)
#함수() #TypeError: 함수() missing 1 required positional argument: '문자열'

#214. 아래와 같은 에러가 발생하는 원인을 설명하라.
def 함수(a, b) :
    print(a + b)
#함수("안녕", 3) #TypeError: must be str, not int

#215. 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
def print_with_simle(string):
    print(string,":D")

#216. 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.
print("#216--------------------------------")
print_with_simle("안녕하세요.")

#217. 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라
# def print_upper_price():
#     print(int(input("#217. 현재가를 입력하시오: "))*1.3)
# print_upper_price()
print("#217--------------------------------")
def print_upper_price(price) :
    print(price * 1.3)
print_upper_price(1000)

#218. 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
print("#218--------------------------------")
def print_sum(a, b):
    print("#218 %d + %d = %d" %(a,b,a+b))
print_sum(3,4)

#219. 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
print("#219--------------------------------")
def print_arithmetic_operation(a, b):
    print(a + b)
    print(a - b)
    print(a*b)
    print(a/b)
print_arithmetic_operation(4, 4)

#220. 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.
print("#220--------------------------------")
def print_max(a,b,c):
    if a > b :
        if a > c :
            print(a)
        else:
            print(c)
    elif b > a :
        if b > c :
            print(b)
        else:
            print(c)
    else:
        print(c)
print_max(1,2,3)

#221. 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
print("#221--------------------------------")
def print_reverse(string) :
    print(string[::-1])
print_reverse("python")

#222. 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
print("#222--------------------------------")
# def print_score(num1,num2,num3) :
#     sum = (num1+num2+num3)/3
#     print(sum)
def print_score(score_list) :
    print(sum(score_list)/len(score_list))
print_score([1,2,3])

#223. 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
print("#223--------------------------------")
def print_even(list_even):
    for i in list_even :
        if i%2 == 0:
            print(i)
print_even ([1, 3, 2, 10, 12, 11, 15])

#224. 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
print("#224--------------------------------------------------")
def print_keys(key):
    for keys in key.keys():
        print(keys)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})

#225. my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.
print("#225------------------------")
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key(dics, values):
    print(dics[values])
print_value_by_key  (my_dict, "10/26")

#226. 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
print("#226------------------------")
def print_5xn(string):
    print(string[:5]+"\n"+string[5:])
print_5xn("아이엠어보이유알어걸")

#227. 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
print("#227----------------------------")
def print_mxn(string, value):
    lens = int(len(string)/3)
    for i in range(lens+1):
        print(i)
        print(string[i*value: i*value+value] )
print_mxn("아이엠어보이유알어걸", 3)

#228. 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
print("#228----------------------------")
def calc_monthly_salary(salary):
    m_salary = int(salary/12)
    print(m_salary)
calc_monthly_salary(12000000)

#229. 아래 코드의 실행 결과를 예측하라.
print("#229----------------------------")
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)
my_print(a=100, b=200)  # 왼쪽: 100, 오른쪽: 200

#230. 아래 코드의 실행 결과를 예측하라.
print("#230----------------------------")
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)
my_print(b=100, a=200) #왼쪽 200, 오른쪽 100

#231. 아래 코드의 실행 결과를 예측하라.
print("#231----------------------------")
def n_plus_1 (n) :
    result = n + 1
n_plus_1(3)
#print (result) #함수 밖에서 호출 불가

#232. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
print("#232----------------------------")
def make_url(url):
    domain = "www."+url+".com"
    print(domain)
make_url("naver")
#www.naver.com

#233. 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
print("#233----------------------------")
def make_list(str):
    #print(list(str))
    list = []
    for i in str :
        list.append(i)
    #print(list)
    return list
make_list("abcd")

#234.숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
print("#234----------------------------")
def pickup_even(val):
    list = []
    for i in val:
        if i%2 == 0:
            list.append(i)
    print(list)
pickup_even([3, 4, 5, 6, 7, 8])

#235. 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
print("#235----------------------------")
def convert_int(value):
    conv = int(value.replace(',',''))
    print(conv)
convert_int("1,234,567")

#236. 아래 코드의 실행 결과를 예측하라.
print("#236----------------------------")
def 함수(num) :
    return num + 4
a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)  #22

#237. 아래 코드의 실행 결과를 예측하라.
print("#237----------------------------")
def 함수(num) :
    return num + 4
c = 함수(함수(함수(10)))
print(c)  #22

#238. 아래 코드의 실행 결과를 예측하라.
print("#238----------------------------")
def 함수1(num) :
    return num + 4
def 함수2(num) :
    return num * 10
a = 함수1(10) #14
c = 함수2(a) #140
print(c) #140

#239. 아래 코드의 실행 결과를 예측하라.
print("#239----------------------------")
def 함수1(num) :
    return num + 4
def 함수2(num) :
    num = num + 2
    return 함수1(num)
c = 함수2(10) #16
print(c)

#240. 아래 코드의 실행 결과를 예측하라.
print("#240----------------------------")
def 함수0(num) :
    return num * 2
def 함수1(num) :
    return 함수0(num + 2)
def 함수2(num) :
    num = num + 10
    return 함수1(num)
c = 함수2(2) #28
print(c)

#241. 현재시간 datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.
print("#241----------------------------")
import datetime
now = datetime.datetime.now()
print(now)

#242 현재시간의 타입 datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.
print("#242----------------------------")
import datetime
def now():
    return datetime.datetime.now()
print(now, type(now))

#243 timedelta datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.
print("#243----------------------------")
import datetime
now = datetime.datetime.now()
for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)

#244 strftime 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.
print("#244----------------------------")
import datetime
#now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))

#245 strptime datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다.
# "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.
print("#245----------------------------")
import datetime
day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))

#246 sleep 함수 time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.
print("#246----------------------------")
import time
import datetime

#while True:
for i in range(3):
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)

#247 모듈 임포트, 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.
print("#247----------------------------")
print("1. import로 임포트, 2. from으로 임포트, ")

#248 os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.
print("#248----------------------------")
import os
ret = os.getcwd()
print(ret, type(ret))

#249 rename 함수, 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.
print("#249----------------------------")
import os
def rename():
    #os.rename("C:/Users/jh/Documents/GitHub/python/rename2.txt", "C:/Users/jh/Documents/GitHub/python/rename.txt")
    pass
rename()

#250 numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.
print("#249----------------------------")
import numpy
for i in numpy.arange(0, 1, 0.1):
    print(i)

#251 클래스, 객체, 인스턴스에 대해 설명해봅시다.

#252 클래스 정의, 비어있는 사람 (Human) 클래스를 "정의" 해보세요.
# class Human:
#     def __init__(self):
#         print("메롱")
# print(Human)

#253 인스턴스 생성, 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.
# class Human:
#     def __init__(self):
#         print("areum")
# areum = Human()

#254 클래스 생성자-1, 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.
class Human:
    def __init__(self):
        print("응애응애")
areum = Human()

#255 클래스 생성자-2, 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.
#areum = Human("아름", 25, "여자")
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print("이름: {} 나이: {} 성별: {}" .format(self.name, self.age, self.sex))
        # print("이름: ", ret.name)
        # print("나이: ",ret.age)
        # print("성별: ", ret.sex)
         #print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def __del__(self):
        print("나의 죽음을 알리지 말라")

ret = Human("불명", "미상", "모름")

#256 인스턴스 속성에 접근
#255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.
#이름: 조아름, 나이: 25, 성별: 여자

#257 클래스 메소드 - 1, 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.
ret.who()
#이름: 조아름, 나이: 25, 성별: 여자

#258 클래스 메소드 - 2, 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.
ret.setInfo("조아람", 25, "여자")
ret.who()

#259 클래스 소멸자, 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.
del(ret)

#260 에러의 원인,아래와 같은 에러가 발생한 원인에 대해 설명하세요.
class OMG : 
    def print() :
        print("Oh my god")
myStock = OMG()
myStock.print()
