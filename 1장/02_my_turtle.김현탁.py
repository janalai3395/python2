"""
    작성일 : 2023년 09월 13일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : 터틀로 그림그리기
"""

import turtle as t  # 터틀 모듈을 사용하기 위한 준비

# turtle 클래스 객체를 t로 생성. (별명)

# 선그리기
t.shape("turtle")
t.speed(2)
# t.forward(200)  # 200 픽셀이동.

# 삼각형 그리기
# t.forward(200)  # 200 픽셀 만큼 이동.
# t.left(120)  # 왼쪽으로 120 도 회전.
# t.forward(200)  # 200 픽셀 만큼 이동.
# t.left(120)  # 왼쪽으로 120 도 회전.
# t.forward(200)  # 200 픽셀 만큼 이동.
# t.left(120)  # 왼쪽으로 120 도 회전.

# 반복문으로 삼각형 그리는 코드 작성
for i in range(9):
    t.forward(200)  # 200 픽셀 만큼 이동.
    t.left(360 // 9)


t.mainloop()  # 그림판을 안없어지게 해줌.
