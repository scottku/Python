def define_list():
    """ 리스트 정의 연습 """
    lst1 = list() # 빈 리스트
    print(lst1, type(lst1))
    lst2 = [] #[]
    lst3 = [1, 2, "python"]
    print(lst2, lst3)
    lst4 = list("python") # 다른 시퀀스 객체를 리스트로 반환
    print(lst4)

def list_oper():
    """
     리스트의 연산
        순차형의 모든 기능 수행
        mutable -> 내부 데이터 변경 가능
    """
    lst = [1, 2, "Python"]

    # 길이의 확인
    print(lst, "length: ", len(lst))
    # 인덱싱
    print(lst[0], lst[1], lst[2]) # 정인덱스
    print(lst[-1], lst[-2], lst[-3]) # 역인덱스


    # Slicing
    print(lst[1:3]) # 항상 경계에 유의
    print(lst[1:]) # 끝 경계가 생략 -> 긑까지
    print(lst[:3]) # 시작 경계 생략 -> 처음부터
    print(lst[:]) # 양 경계 생략 -> 전체

    copy = lst[:] # 슬라이싱을 이용한 리스트 전체의 복사
    print(copy is lst) # 슬라이싱 -> 별도의 객체 생성(False)

    # 연결(+) = 원본을 변경하지 않고 두 list를 연결한 새 객체 생성
    #   vs extend : 원본 뒤에 다른 리스트 연장 -> 내부 데이터 변경
    print(lst + ["Java", True, 3.141592])
    print("원본: ", lst)

    # append vs extend
    copy.append(["Java", True, 3.141592]) # 개별 요소의 추가 (리스트를 통째로 한 요소로서 추가)
    print(copy)
    copy.extend(["Java", True, 3.141592]) # 다른 list를 연결하여 확장
    print("Extend: ", copy)

    # insert
    copy.insert(2, [1, 2, 3]) # 2번 index에 요소 삽입
    print("INSERT: ", copy)

    # 반복(*)
    print("원본: ", lst)
    print("반복: ", lst * 3)

    # 포함여부 확인: in, not in
    print('Python' in lst) # list에 파이썬이 포함되어 있는가?
    # index의 확인

    if "Python" in lst:

        print("INDEX: ", lst.index("Python")) # 없는 객체 생성시 ValueError

    print("COPY: ", copy)

    # 항목의 개수
    print("count: ", copy.count("Python"))

    # 삭제 del
    del copy[0]
    print("CoPY: ", copy)
    # 삭제 remove
    del copy[0] # copy.remove(3.14159)
    copy.remove(3.141592)
    print("Remove: " , copy)

    # 슬라이싱 이용한 치환
    # 메서드 이용보다 슬라이싱 이용 치환 방법 먼저 이용하기를 권장
    lst = [1,12,123,1234,12345]
    print("원본:", lst)
    lst[0:2] = [10, 20]
    print(lst)
    # 슬라이싱을 이용한 삭제
    lst[0:2] = [] # 슬라이싱 범위에 빈 리스트 할당
    print(lst)
    # 슬라이싱을 이용한 삽입
    lst[1:1] = ["inserted"] # 중간에 삽입
    print(lst)
    # 맨 마지막에 삽입
    lst[4:] = ["appended"] # 맨 뒤에 삽입
    print(lst)
    # 맨 앞에 삽입
    lst[:0] = ["prepended"] # 맨 앞에 삽입
    print(lst)

    # 다양한 기초 산술 함수 제공
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("SUM: " , sum(lst))
    print("MIN: ", min(lst))
    print("MAX: ", max(lst))
    print("Average: ", sum(lst)/len(lst)) # AVG 메서드는 없음

def list_method():
    """ 리스트 메서드들 """
    lst = [10, 2, 22, 9, 8, 33, 4, 12]
    print("원본: ", lst)
    copy = lst.copy()   # 복제 메서드
    # Reverse : 리스트의 반전
    copy.reverse()
    print("Reverse: ", copy)

    copy = lst.copy()
    print("원본: ", copy)

    # 정렬: sort
    # 메서드로서의 sort -> 내부 데이터를 실제 sort
    # 문법으로서의 sorted -> 정렬된 새 리스트를 반환

    result = sorted(copy) # copy를 정렬 -> 새 리스트로 반환
    print("Sorted ASC: ", result)   # 오름차순
    result = sorted(copy,reverse=True) # 내림차순 정렬
    print("Sorted DESC: ", result)
    # 정렬 키 함수 정의
    # 정렬 키 함수를 전달 -> 정렬 기준을 변경
    print("원본: ", copy)
    result = sorted(copy, key=str) # 키 함수를 str로 변경
    print("Sorted key=str: ", result) # 문자열은 앞글자가 가장 빠른것부터 정렬 -> 1~9
    # 정렬 기준의 사용자 정의
    # 리스트의 요소를 5로 나눈 나머지의 역순으로 정렬
    def key_func(val): # 사용자 정의 키 함수
        return val % 5
    result = sorted(copy, key=key_func, reverse=True)

    print("Sorted key=custom, DESC: ", result)

    # sorted 함수 -> 원본을 변경시키지 않음
    # sort 메서드 -> 원본 내부 데이터를 변경
    copy.sort(key=key_func, reverse=True)
    print("Sort Method: ", copy)

def stack_ex():
    """ 리스트를 활용한 스택의 구현
            append, pop 메서드
    """
    stack = []
    stack.append[10]
    stack.append[20]
    stack.append[30]
    print("Stack: ", stack)

    # 인출
    print("Pop ", stack.pop())
    print("Pop: ", stack.pop())
    print("Pop: ", stack.pop())
    print("Pop: ", stack.pop())
    if len(stack): # 스택이 비어있지 않으면
        print("POP: ", stack.pop())
    else:
        print("스택이 비어있습니다")

def qeueu_ex():
    """ 리스트를 활용한 queue의 구현
            append, pop(0)을 활용 구현
            First Input First Output 자료형 """

    queue = []
    queue.append(10)
    queue.append(20)
    queue.append(30)

    print("QERER: ", queue)

    # 인출: pop(0)
    print(queue.pop(0)) # 맨 앞에서부터 인출
    print(queue.pop(0))
    print(queue.pop(0))


if __name__ == "__main__":
    # define_list()
    # list_oper()
    # list_method()
    # stack_ex()
    qeueu_ex()
