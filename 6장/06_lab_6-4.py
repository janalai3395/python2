"""
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : LAB 6-4 리스트에서 최솟값, 최대값을 찾아 출력하는 함수
    
    리스트에 10개의 값을 랜덤으로 생성하고,
    max 또는 min을 입력받아 최대, 최소값을 찾아 돌려주는 함수

    (함수)
            5) 두 값을 전달받아 매개 변수에 저장.
            6) 최대값, 최소값을 찾는다.
            7) 값을 돌려준다.

    (메인)
        1.무한반복
            1) 랜덤으로 10~99 까지 10개의 수를 리스트로 생성
            2) 생성된 리스트를 출력
            3) 사용자로부터 최대값을 알고 싶은지 최소값을 알고 싶은지 묻는다.
                사용자가 입력할 값은 max 또는 min
            4)  입력받은 max 또는 min과 생성된 리스트 가지고 함수 호출
            8) 돌려 받은 최대값 또는 최소값을 출력한다.

"""

import random


def max_min(list, mathod):
    while True:
        mathod = input("min 또는 max 를 입력해주세요 (table(테이블보기) reset(리셋하기)) : ")
        if mathod == "min":
            print(f"{min(list)}")
        elif mathod == "max":
            print(f"{max(list)}")
        elif mathod == "table":
            print(list)
        elif mathod == "reset":
            list = []
            for i in range(10):
                num2 = random.randint(10, 99)
                list.append(num2)
            print("리셋되었습니다.")
        else:
            break


list1 = []

for i in range(10):
    num2 = random.randint(10, 99)
    list1.append(num2)

max_min(list1, 0)
