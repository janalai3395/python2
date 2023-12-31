"""
    작성일 : 2023년 09월 20일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : 선택문 if~else
            년도를 입력받아 윤년인지 아닌지 판단하는 프로그램
            1.4로 나눠지면 윤년
            2.100년마다 평년이 옴 (윤년X)
            3.400년마다 는 또 윤년임
"""
year = int(input("연도를 입력해주세요."))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # 윤년인지 아닌지 판별하는 코드
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 평년입니다.")
