def quiz_01():
    score1 = input("점수를 입력하세요: ")
    score2 = input("점수를 입력하세요: ")
    if (int(score1) >= 50) & (int(score2) >= 50):
        if (int(score1)+int(score2))/2 >= 60:
            print("합격")
        else:
            print("불합격")
    else:
        print("불합격")

def quiz_02():
    for i in range(1, 10):
        print(i, "단")
        for j in range(1, 10):
            print(i, " x ", j, " = ", i*j)
        print()

def quiz_03():
    balance = 0
    while True:
        str1 = input("알파벳을 입력해 주세요: ")
        if str1 == "q":
            break
        if str1 != "d" and str1 != "w":
            print("?")
            continue
        if str1 == "d" or "w":
            money = input("금액을 입력해 주세요: ")
            if str1 == "d":
                balance += int(money)
                print("Amount: ", money, "\n", "Balance: ", balance)
            elif str1 == "w":
                balance -= int(money)
                print("Amount: ", money, "\n", "Balance: ", balance)





if __name__ == "__main__":
    # quiz_01()
    # quiz_02()
    quiz_03()
