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

""" # End of Code
#180 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):
    #print(low_prices[i], high_prices[i])
    #volatility = (high_prices[i]-low_prices[i])
    volatility.append(high_prices[i] - low_prices[i])
    print(volatility)