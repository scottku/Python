numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
evens = {0, 2, 4, 6, 8}
odds = {1, 3, 5, 7, 9}
mthree = {0, 3, 6, 9}

def define_set():
    """ SET 정의 연습 """
    empty = set() # 빈 집합
    print(empty, type(empty))
    empty = {} # -> 빈 dictionary 취급
    print(empty, type(empty))

    # 순서가 없고(인덱스 없음), 슬라이싱 불가
    # 길이(요소의 수), 포함 여부(in, not in) 정도만 사용 가능
    print(numbers, "Length: ", len(numbers))
    print("포함 여부 확인: ", 2 in numbers, 2 in evens, 2 in odds)

    # 캐스팅 : 다른 순차형으로 세트 만들기
    s = "Python Programming" # 문자열 안쪽에 모두 몇 개의 알파벳이 사용되었는가?
    chars = set(s.upper())
    print(s, chars) # 중복 x, 순서 x -> list 등의 중복값 삭제에 유용
    lst = "Python Programming Java Programming".upper().split()
    print(list) # Programming 중복값

    words = set(lst)
    print(words, len(words))

def set_methods():
    """ SET의 메서드 """
    print("전체 집합: ", numbers)
    # 요소의 추가
    numbers.add(10) # 10 요소를 추가
    print(numbers)
    evens.add(10)
    print(evens)
    evens.add(4)
    print("짝수 집합(중복?): ", evens) # 중복 허용x
    # 삭제 : discard, remove
    evens.discard(4)
    print("짝수 집합: ", evens)
    evens.discard(4)
    print("짝수 집합: ", evens) # 없는 요소를 삭제해도 에러 x
    # evens.remove(4)
    # print("짝수 집합: ", evens) 없는 요소 삭제시 key 에러
    # 집합 업데이트
    evens.update({2, 4, 6})
    print("짝수 집합: ", evens)

def set_oper():
    """ 판별 연산
            모집합 여부, 부분 집합 여부
    """

    # 짝수 집합 합집합 홀수 집합 == 전체 집합
    print("짝수 합 홀수: ", evens.union(odds) == numbers)
    print("짝수 합 홀수: ", evens | odds == numbers)

    # 모집합, 부분집합 판별
    print("전체집합이 짝수 집합의 모집합?", numbers.issuperset(evens))
    print("홀수집합이 전체집합의 부분집합?", odds.issubset(numbers))

    # 교집합
    print("짝수집합 교집합 3의 배수집합: ", evens.intersection(mthree))
    print(mthree & odds == {3, 9})

    # 차집합
    print("전체집합 차집합 짝수 집합: ", numbers.difference(evens))
    print("전체집합 차집합 짝수 집합 -> 홀수 집합?", numbers - evens == odds)

def loop():
    # numbers를 순회하면 출력
    for item in numbers:
        print(item, end=" ")
    else:
        print()

if __name__ == "__main__":
    # define_set()
    # set_methods()
    # set_oper()
    loop()