"""
    작성일 : 2023년 09월 13일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : 직각 삼각형의 빗변의 길이를 구하시오.
"""
height = int(input("높이를 입력하세요."))
base = int(input("밑변을 입력하세요."))
print(
    "높이가 {} 밑변이 {} 일떄 직각 삼각형의 빗변의 길이는 {} 입니다.".format(
        height, base, (height**2 + base**2) ** (1 / 2)
    )
)
