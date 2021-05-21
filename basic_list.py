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
    print("Average: ", sum(lst)/len(lst))

if __name__ == "__main__":
    # define_list()
    list_oper()
