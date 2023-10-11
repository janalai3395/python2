"""
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : 여러개의 값을 넘겨주고 여러개의 값을 돌려 받기.

    두 수를 전달받아 사칙 연산의 결과값을 돌려주는 함수.

    [알고리즘]
    (함수)
        3.두 수를 전달받아 매개변수에 저장한다.
        4.두 수를 가지고 사칙연산을 한다.
        5.계산된 합을 함수를 호출한 곳으로 돌려준다.

    (메인)
        1.두 수를 입력받는다.
        2.두 수를 가지고 함수를 호출한다.
        6.돌려받은 값을 출력한다.
"""


# 함수 선언
def calculater(first, second):
    sum = first + second
    sub = first - second
    multi = first * second
    divide = first / second
    rest = first % second
    return sum, sub, multi, divide, rest


first = int(input("첫 번째 수 입력 : "))
second = int(input("두 번째 수 입력 : "))

sum, sub, mul, div, rest = calculater(first, second)
print(f"{first} + {second} = {sum}")
print(f"{first} - {second} = {sub}")
print(f"{first} * {second} = {mul}")
print(f"{first} / {second} = {div}")
print(f"{first} % {second} = {rest}")
