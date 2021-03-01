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





