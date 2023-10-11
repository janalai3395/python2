"""
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : 함수의 디폴트 인자
"""


def order(num, pickle, onion):
    print(f"햄버거 {num}개 - 피클{pickle}, 양파{onion}")


# order(1) # 오류발생. 인자는 1개인데 매개변수는 3개이다.

# 인자가 부족한 경우 기본밗을 넣어 주는 것 => 디폴트 인자


def order2(num, pickle="기본", onion="기본"):
    print(f"햄버거 {num}개 - 피클{pickle}, 양파{onion}")


order2(2)
order2(1, pickel='뺌', onion='기본')