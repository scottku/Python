def define_dict():
    """ 사전 생성 연습 """
    # 빈 사전
    dct = dict()
    print(dct, type(dct))
    # Literal : {} 이용
    dct = {"basketball": 5, "baseball": 9}

    # 순서 없고, 인덱스가 아닌 키를 이용해서 내용에 접근
    dct['volleyball'] = 6
    print(dct)

    # 길이 확인 가능 -> 키 목록을 대상으로 길이 확인
    # 연결, 반복 지원 x
    print("Length of dct: ", len(dct))
    print("soccer 키가 있는가?", "soccer" in dct)
    print("baseball 키가 있는가?", "baseball" in dct)

    # 키의 목록, 값의 목록
    print("키의 목록: ", dct.keys(), type(dct.keys())) # dict_keys는 거의 set과 비슷
    print("값의 목록: ", dct.values(), type(dct.values())) # dict_values도 거의 list와 비슷
    print("(키, 값) 쌍 튜플 목록: ", dct.items(), type(dct.items()))

    # 응용
    # 포함 여부는 key를 대상으로 한다
    # 사전의 값의 포함 여부를 확인?
    # dct 값 중에서 9가 포함되어 있는가?
    print("9가 값의 목록에 있는가?: ", 9 in dct.values())

    # 키워드 인자를 이용한 사전의 생성
    d1 = dict(key1="value1", key2="value2")
    print(d1, type(d1))

    # 튜플의 리스트를 이용한 사전의 생성
    d2 = dict([('key1', 'value1'), ('key2', 'value2')])
    print(d2, type(d2))

    # 키 목록, 값 목록 있을 때 -> zip 객체 이용
    keys = ('one', 'two', 'three')
    values = (1, 2, 3, 4)
    d3 = dict(zip(keys, values))
    print(d3, type(d3))

    # 사전의 키: 변경 불가 객체만 사용 가능
    d4 = {}
    d4[True] = "true"
    d4[10] = 10
    d4["eleven"] = 11
    d4[(10, "홍길동")] = 100
    # list 등 가변 객체는 키로 사용 불가
    # d4[[1,2,3]] = 1000 -> unhashable type

def dict_methods():
    """ 사전의 메서드 """
    dct = {"soccer": 5, "baseball": 9, "volleyball": 6}
    print(dct)
    # 사전의 키의 목록 : keys()
    keys = dct.keys()
    print("키 목록: ", keys, type(keys))
    # dict_keys 역시 순차형 -> 다른 순차형으로 변환 가능
    lst_keys = list(keys) # dict_keys -> list로 type 변환
    print(lst_keys, type(lst_keys))

    # 사전의 값의 목록: values()
    values = dct.values()
    print("값의 목록: ", values, type(values))
    # dict_values 역시 순차형
    lst_values = list(values)
    print(lst_values, type(lst_values))

    # 쌍 튜플의 목록: items()
    items = dct.items()
    print("(키, 값)의 목록: ", items, type(items))
    lst_items = list(items)
    print(lst_items, type(lst_items))

    # 튜플의 리스트 -> 인덱스 접근 가능
    print("KEY: ", lst_items[0][0], "Value: ", lst_items[0][1])

    # 사전 비우기
    dct.clear()
    print(dct)

def using_dict():
    phones = { "둘리": "010-1234-5678", "도우너": "010-9876-5432", "또치": "010-2222-3333"}
    print(phones)

    # 새로운 항목의 추가
    phones['고길동'] = "032-1234-5678"
    print(phones)

    # 키에 접근 vs get() 메서드
    print("둘리", phones["둘리"])
    # print("홍길동", phones["홍길동"]) # 없는 키에 접근 -> KeyError
    print("홍길동", phones.get("홍길동")) # -> None 반환
    # get() 메서드를 사용하는 이유
    #   1. key가 없어도 오류 없이 None "값"을 할당 받을 수 있음
    #   2. 기본값 기능이 있어 None 값을 받고 싶지 않을 때
    print("홍길동", phones.get("홍길동", "전화 없음")) # 키가 없으면 기본값 반환

    # 삭제: del
    del phones["도우너"] # 도우너 키 삭제
    print(phones)
    # 값을 가져오며 삭제: pop
    print(phones.pop("둘리"))
    print(phones)

def loop():
    """ 리스트 순회 """
    words = "Life is too short, you need Python.".replace(",", "").upper().split()
    print("List: ", words)

    # 순차 자료형은 for ~ in 문으로 차례대로 요소를 전달 받을 수 있다. (별도 인덱스 변수는 없음)
    for word in words:
        print("WORD: ", word)

    phones = {"둘리": "010-1234-5678", "도우너": "010-9876-5432", "또치": "010-2222-3333"}
    print(phones)

    # 기본적인 루프 -< 기본은 Key의 목록
    for key in phones:
        print(key + ":" + phones.get(key))
    print()

    # 사전으로부터 키의 목록을 리스트로 받아온 후 루프
    for key in phones.key():
        print(key + ":" + phones.get(key))
    print()

    # 키와 값 쌍 튜플을 받아와서 언패킹
    for (key, value) in phones.items():
        print(key + ":" + value)

if __name__ == "__main__":
    # define_dict()
    # dict_methods()
    # using_dict()
    loop()