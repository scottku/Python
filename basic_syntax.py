# 연산자 연습
def arith_oper():
    print("===== 산술 연산 =====")
    # +, - , *, /
    print(7/3)

    # // : 정수 나눗셈의 몫연산자
    print(7//3) # 정수 나눗셈의 몫
    print(7%3)  # 정수 나눗셈의 나머지

    # divmod 함수 : 목과 나머지 동시에 구하기
    print(divmod(7,3)) # 7을 3으로 나눈 몫과 나머지

    print(divmod(7, 3)[0]) # 몫
    print(divmod(7, 3)[1]) # 나머지

    # 제곱 연산자 : **
    print(7*3) #7의 3승
    print(pow(7,3)) #내장 수치 제곱함수

def complex_ex():
    print("========== 복소수")
    print(3+4j) # 복소수
    print(3+4j.real) #실수부 반환
    print(3+4j.imag) #허수부 반환
    print(3+4j)

    print(complex(3, 4)) # 타입 함수를 이용한 복소수 선언

def rel_oper():
    print("==비교연산==")
    print("1 > 3 ?", 1 > 3)
    print("1 < 3 ?", 1 < 3)
    print("6 equals 9 ?", 6 == 9)
    print("6 not equals 9?", 6 != 9)

    s1 = "Python"
    s2 = "Python"

    print("문자열의 ==", s1 == s2)

    ## 복합 관계식
    a = 6
    # a가 0보다 크고 10보다 작은가?
    print(a > 0 and a < 10) # 논리곱
    print(0 < a and a < 10)
    print(0 < a < 10)

    # 수치형 이외 다른 타입의 비교
    print("문자열의 대소: ", "abcd" > "abd")
    print("튜플의 대소: ", (1,2,4) > (1,3,1))
    print("리스트의 대소: ", [1,2,4]>[1,3,1])

    # 동질성의 비교 ==
    # 동일성의 비교 is
    a = 10
    b = 29
    c = a
    print("a == b? : ", a==b)
    print("a = b? : ", a is b)
    print("a == c? : ", a==c)
    print("a is c? : ", a is c)

def variable_ex(): # 변숭
    print("========== 변수")
    # 변수명은 문자, 숫자, _의 조합
    # 숫자로 시작은 안됨
    # 예약어 사용 불가
    import keyword # keyword 모듈 로드
    print(keyword.kwlist)
    print("키워드 갯수: ", len(keyword.kwlist))

    # 유니코드 이름의 변수도 사용가능 -> 권장하지는 않는다
    가격 = 12000
    print(가격 + 가격*0.1)

def assignment_ex(): #치환문
    print("========== 치환문")
    
    # 여러 변수를 한꺼번에 할당
    a, b = 3.5, 5.3 # 좌변의 변수의 개수와 우변의 값의 개수가 동일할 것
    print(a, b)
    
    # 값 교환
    a, b = b, a
    print(a, b)
    
    # 같은 값을 여러 변수에 동시 할당
    x = y = z = 2021
    
    # 중요 : 동적 타이핑
    # 파이썬은 변수 선언이 없고, 값이 할당될 때 데이터 타입 결정
    a = 1
    print(a, "is", type(a)) # type 함수 -> 데이터 혹은 객체의 데이터 타입 확인
    a = "Hello Python"
    print(a, "is", type(a))

    # isinstance(판별할 값 or 객체, 데이터 타입)
    print("a는 str의 객체? : ", isinstance(a, str))

def logical_oper():
    print("========== 논리연산")
    # 논리곱(and : 둘 다 True 일 때만 True)
    # 논리합(Or : 둘 중 하나만 True면 True)
    # 논리정(not : True<=>False
    a, b = 20, 30
    print(not a < b) #a < b의 논리를 부정
    print(a < b and a != b) # a < b의 논리값과 a !=b의 논리값의 논리곱
    print(a == b or a != b) # a == b의 논리값과 a != b의 논리값의 논리합


if __name__ == "__main__":
    #arith_oper()
    #rel_oper()
    #variable_ex()
    #assignment_ex()
    logical_oper()
