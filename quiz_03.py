def quiz_01():
    x = input("수를 입력하세요: ")
    while True:
        try:
            y = int(x)
        except ValueError:
            x = input("정수가 아닙니다. 수를 다시 입력하세요: ")
            continue
        else:
            break
    total = 0
    for i in range(0, y+1):
        if i % 3 == 0:
            total += i
    """ lst = [i for i in range(1, to + 1) if i % 3 == 0]
        total = sum(lst) """

    print("1부터 ", y, "까지 3의 배수의 합 = ", total)

def quiz_02():
    lst = [1, 3.14, 'python', 7, 89.1, 3]
    lst_cleaned = []
    for i in lst:
        if isinstance(i, (int, float)):
            lst_cleaned.append(i)
    print(lst_cleaned)

def quiz_03():
    def summary(*args):
        total = 0
        for i in args:
            total += i
        maxval = max(args)
        minval = min(args)
        gs = 0
        for i in args:
            gs += 1
        avg = total / gs
        print(total, maxval, minval, avg)

    summary(1, 3, 80, 55, 37)

def quiz_04():
    s = """We encourage everyone to contribute to Python. 
If you still have questions after reviewing the material
in this guide, then the Python Mentors 
group is available to help guide new contributors through the process."""
    S = s.replace(',', '').replace('.', '').replace('\n', '').upper().split()
    # print(S)
    RE = {}
    for strings in S:
        RE[strings] = RE.get(strings, 0) + 1
        keys = sorted(RE.keys())
    for strings in keys:
        print(strings + ":" + str(RE[strings]))





if __name__ == "__main__":
    # quiz_01()
    # quiz_02()
    # quiz_03()
    quiz_04()