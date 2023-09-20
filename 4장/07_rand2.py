"""
    작성일 : 2023년 09월 20일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : 선택문 if~else
            random 을 이용한 가위바위보 게임.
            0 = 가위
            1 = 바위
            2 = 보

            두명의 플레이어의 이름을 입력받아
            가위 바위 보 게임을 진행합니다.
"""
import random  # 랜덤 함수 가져오기

print("가위 바위 보 게임 시작")
num1 = random.randrange(3)  # 랜덤으로 0,1,2 생성
num2 = random.randrange(3)  # 랜덤으로 0,1,2 생성
player1 = input("첫번쨰 플레이어의 이름을 입력해주세요 : ")
player2 = input("두번쨰 플레이어의 이름을 입력해주세요 : ")

print(player1, " : ", end="")
if num1 == 0:
    print("가위")
elif num1 == 1:
    print("바위")
else:
    print("보")

print(player2, " : ", end="")
if num2 == 0:
    print("가위")
elif num2 == 1:
    print("바위")
else:
    print("보")
# 승자 판단 출력
if num1 == num2:  # 비겼을 경우
    print(f"{player1} 와 {player2} (은)는 비겼습니다")
elif (
    (num1 == 0 and num2 == 2) or (num1 == 1 and num2 == 0) or (num1 == 2 and num2 == 1)
):  # player 1 이 이겼을경우
    print(f"{player1} 이(가) {player2} 에게 승리하였습니다.")
else:
    print(f"{player2} 이(가) {player1} 에게 승리하였습니다.")
