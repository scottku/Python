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

if __name__ == "__main__":
    define_dict()