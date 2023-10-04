"""
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 :  심화문제 5.2, 141쪽  
            두 수를 입력 받아
            1.  두수 사이의 합계 출력하기
            2. 두 수 사이의 짝수의 합계 출력하기
"""
num1 = int(input("첫번째 숫자를 입력해주세요 : "))
num2 = int(input("두번째 숫자를 입력해주세요 : "))
sum1 = 0
sum2 = 0

if num1 > num2:  # num1 이 더 클떄 바꿔주는 코드
    num1, num2 = num2, num1
for i in range(num1, num2 + 1):  # 두 수 사이의 합계를 출력하는 코드
    sum1 += i
print("두 수 사이의 합계 : ", sum1)
for i in range(num1, num2 + 1):  # 두 수 사이의 짝수의 합계를 출력해주는 코드
    add = +i
    if add % 2 == 0:
        sum2 += add
print("두 수 사이의 짝수의 합계 : ", sum2)
