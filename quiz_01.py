def quiz_01():
    str1 = "Life is too short, you need Python"
    lst = list(str1.lower().replace(",", "").replace(" ", ""))
    chars = set(lst)
    print(chars)
    lst = list(chars)
    print(len(sorted(lst)))

def quiz_02():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    slice1 = lst[3:7]
    del lst[3:7]
    slice2 = reversed(slice1)
    lst[3:3] = slice2
    print(lst)

def quiz_03():
    students = [{"name": "Kim", "kor": 80, "eng": 90, "math": 80},
    {"name": "Lee", "kor": 90, "eng": 85, "math": 85}]
    total1 = 0

    print(list(students[0].values()))
    lst1 = list(students[0].values())
    print(list(students[1].values()))
    lst2 = list(students[1].values())
    for i in range(1, 4):
        total1 += lst1[i]
        print(total1)
    students[0]["total"] = total1
    avg1 = round(total1 / 3, 2)
    students[0]["average"] = avg1

    total2 = 0

    for i in range(1, 4):
        total2 += lst2[i]

    students[1]["total"] = total2
    avg2 = round(total2 / 3, 2)
    students[1]["average"] = avg2
    print(students)








if __name__ == "__main__":
    quiz_01()
    quiz_02()
    quiz_03()