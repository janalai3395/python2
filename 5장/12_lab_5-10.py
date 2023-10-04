"""
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 :  사용자가 입력하는 숫자의 합 계산 lab 5-10
    사용자가 입력한 숫자들을 더하는 프로그램을 작성하는데 yes라고 답한 동안에만 숫자를 입력받는다.

    
    #만약 break 문을 사용한다면

    sum = 0  # 합계
    while True :
        num = int(input("숫자를 입력하시오 : "))  # 숫자를 입력받는 줄
        sum += num  # sum에 입력받은 숫자를 더함
        answer = input("계속 ? (yes/no) : ")  # 대답을 입력받아서 yes가 아닐시 반복함
        if answer != "yes"
            break
    print(f"합계 : {sum}")  # 마지막으로 출력하는 부분


"""

sum = 0  # 합계
answer = "yes"  # 조건
while answer == "yes":  # 조건식
    num = int(input("숫자를 입력하시오 : "))  # 숫자를 입력받는 줄
    sum += num  # sum에 입력받은 숫자를 더함
    answer = input("계속 ? (yes/no) : ")  # 대답을 입력받아서 yes가 아닐시 반복함
print(f"합계 : {sum}")  # 마지막으로 출력하는 부분
