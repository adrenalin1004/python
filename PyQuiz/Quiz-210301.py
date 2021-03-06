##########################################
#### 초보자를 위한 파이썬 300제         ####
#### https://wikidocs.net/book/922    ####
##########################################

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