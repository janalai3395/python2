"""
    작성일 : 2023년 09월 20일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : 선택문 if~else
            random 을 이용한 가위바위보 게임.
            0 = 가위
            1 = 바위
            2 = 보
"""
import random  # 랜덤 함수 가져오기

print("가위 바위 보 게임 시작")
num = random.randrange(3)  # 랜덤으로 0,1,2 생성
if num == 0:
    print("가위")
elif num == 1:
    print("바위")
else:
    print("보")
