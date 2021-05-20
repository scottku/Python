def bool_ex(): # bool 자료형
    print("========== bool 연습")
    # 참(True), 거짓(false)
    # 내부적으로 거짓은 0 나머지는 모두 참으로 판단
    # bool의 판정 방법
    print(bool(0), bool(1))
    a = 1
    print(a > 10) # 논리 연산 or 비교 연산으 결

    b = a == 1
    print(b, type(b))

    print(b + 10)

    # bool은 bool의 객체인가?
    print(isinstance(True, bool)) # True is bool?
    print(isinstance(True, int)) # True is int? -> int를 상속받아서 bool을 만든 것이라 True.

    # 내부가 비어있으면 거짓, 비어있지 않다면 참
    # bool 캐스팅
    print("정수형: ", bool(10), bool(0))
    print("실수형: ", bool(3.14), bool(0.0))
    print("문자열: ", bool("Python"), bool(""))
    print("순차형: ", bool([1, 2, 3]), bool([]))
    print("Map: ", bool({"a": 2}), bool({}))
    print("None: ", bool(None)) # None : Java의 Null과 비슷 -> 아무 것도 할당되지 않은 상태

    # Circuit Break
    print("CB or 1: ", [1, 2, 3] or []) # (T or F) or는 먼저 나온 True 객체를 선택
    print("CB or 2: ", [] or [1, 2, 3]) # (F or T)
    print("CB and 1: ", [1, 2, 3] and [4, 5, 6] and [7, 8, 9]) # (T and T) and는 True일 시 뒤의 값을 선택
    print("CB and 2: ", [] and [1, 2, 3]) # (F and T) None 반환

def integer_ex():
    print("===== 정수형 연습")
    a = 23 # 실제로 값을 입력하는 Literal 방식
    b = int(23) # type 함수를 이용하는 방식
    print(a, "is", type(a))
    print(b, "는 int의 객체?", isinstance(b, int))

    # 2진, 8진, 16진 정수 표현 가능
    b = 0b1101 # 2진수 0b 접두사
    o = 0o23 # 8진수 0o 접두사
    x = 0xFF # 16진수 0x 접두사

    print(b, o, x)
    
    # 3.x 버전의 파이썬에서는 int, long을 구분하지 않는다
    # long 형의 저장크기인 64bit를 초과하는 정수도 입력 가능하다
    i = 2 ** 2048
    print(i)
    print(i.bit_length()) # i 객체의 비트수 확인

    # 진법 변환 함수
    print(bin(2021))
    print(oct(2021))
    print(hex(2021))

def float_ex():
    # 실수형은 모두 float로 표기
    print("===== 실수형 연습")
    a = 3.14159
    print(a, "is", type(a))
    print(isinstance(a, int))
    b = float(3.0) # type 함수를 이용한 생성
    print(b, "is", type(b))
    # is_integer : 타입 판별이 아니라 값의 형태가 정수형(소숫점 아래 값이 없는지)인지를 판별
    print(a.is_integer(), b.is_integer())

    # 소수점 포함, e, E 지수형태로 표현 가능
    c = 3e3
    d = -2E-5
    print(c, d)
    print(-2E-5 == -0.00002)

def complex_ex():
    print("===== 복소수 연습")
    # 복소수 : 실수부 + 허수부 J 형태
    a = 4+5J    # 실수부 4, 허수부 5인 복소수
    print(a, "is", type(a))
    b = 7-2j    # 실수부 7, 허수부 -2인 복소수
    print(b, "complex의 객체?", isinstance(b, complex))

    # 복소수 -> 수치형 -> 산술연산 가능
    print(a + b)

    print(a, "의 실수부?", a.real)
    print(a, "의 허수부?", a.imag)
    print(a, "의 켤레 복소수?", a.conjugate())

    # 타입 함수를 이용한 복소수의 생성
    c = 7
    d = 3
    e = complex(7, 3) # 실수부가 7, 허수부가 3인 복소수 생성
    print(e, "is", type(e))

def builtin_math_function(): # 내장 수치 함수
    print(abs(-2)) # 절댓값
    print(int(3.14159)) # 타입 함수를 이용한 타입의 변환
    print(float(3))     # 타입 변환
    print(complex(1))
    print(divmod(5, 3)) # 정수 나눗셈의 몫과 나머지 일괄 계산
    print(pow(2, 10))   # == 2 ** 10

if __name__ == "__main__":
    #bool_ex()
    #integer_ex()
    #float_ex()
    #complex_ex()
    builtin_math_function()