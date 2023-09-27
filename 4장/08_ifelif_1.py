"""
    작성일 : 2023년 09월 27일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : 점수를 입력받아 학점을 출력하시오.
            90 ~ 100 점 : A학점
            80 ~ 89 점 : B학점
            70 ~ 79 점 : C학점
            60 ~ 69 점 : D학점
            0 ~ 59 점 : f학점

    알고리즘 : 1. 점수를 입력 받는다.
            2. 판단하여 출력한다.
"""

# 점수를 입력 받는 부분
score = int(input("점수 입력 : "))

# 판별하는 부분.
# 이 코드는 논리 오류가 발생한다. - ex) 300점을 입력받으면 A학점으로 나온다.
print("::: 첫번쨰 성적 처리 :::")
if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60:
    print("D학점")
else:
    print("F학점")

print()  # 빈줄 출력

# 정확한 범위를 지정하자. - 성적의 범위를 벗어나면 잘못된 점수 입력입니다.
print("::: 두번쨰 성적 처리 :::")
if 90 <= score <= 100:
    print("A학점")
elif 80 >= score and score <= 89:
    print("B학점")
elif 70 <= score <= 79:
    print("C학점")
elif 60 <= score <= 69:
    print("D학점")
elif 0 <= score <= 59:
    print("F학점")
else:
    print("점수를 잘못 입력하셨습니다.")

print()

# 점수는 무조건 0~100점 사이입니다. -아니면 잘못된 입력입니다.
print("::: 세번쨰 성적 처리 :::")
if 0 <= score <= 100:  # 범위를 지정해주는 if 문
    if score >= 90:  # 내포된 if 문
        print("A학점")
    elif score >= 80:
        print("B학점")
    elif score >= 70:
        print("C학점")
    elif score >= 60:
        print("D학점")
    else:  # A,B,C,D 학점이 아니면. 0~59 까지의 케이스
        print("F학점")
else:  # 0~100점 사이에 점수가 아니면
    print("점수를 잘못 입력하셨습니다.")
