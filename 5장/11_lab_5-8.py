"""
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : 조건에 따라 반복하는 while문
            교재127p
"""
import turtle as t

# 도전 2번 도형그리기
t.shape("turtle")
i = 0
t.speed(30)
while i < 18:
    t.forward(150)
    t.right(140)
    i += 1

# 도전 3번 별그리기
j = 0
while j < 5:
    t.forward(100)
    t.right((360 / 5) * 2)
    t.forward(100)
    t.left(360 / 5)
    j += 1
t.done()
