numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
evens = {0, 2, 4, 6, 8}
odds = {1, 3, 5, 7, 9}
mthree = {0, 3, 6, 8}

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





if __name__ == "__main__":
    define_set()