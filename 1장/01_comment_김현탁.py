"""
    작성일 : 2023년 09월 13일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : 주석과 출력 함수 사용하기.
"""


# 학과 학번 이름을 저장하시오.


major = "컴퓨터공학부"
id = 23
name = "김현탁"

# 출력한다.
print("학과 : ", major)
print("학번 : {}".format(id))

# 안녕하세요 저는 저는 oo학과 oo학번 oo입니다.
print("안녕하세요. 저는 ", major, "학과 ", id, "학번 ", name, "dlqslek.")
print("안녕하세요. 저는 {} {}학번 {}입니다. ".format(major, id, name))

# python을 10개 출력하시오. 반복문 사용 안함.
print("python \n" * 3)

num1 = "10"
num2 = "20"

print(num1 + num2)
