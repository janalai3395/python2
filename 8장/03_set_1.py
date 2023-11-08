"""
    작성일 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : 집합 set()
"""
# 빈 집합 생성
number = set()

# 숫자 3개로 이루어진 집합
number1 = {2, 1, 3}
print("집합 number1 : ", number1)

# 리스트로부터 집합 생성.
nuber2 = set([1, 2, 3, 1, 2])
print("집합 number2 : ", nuber2)  # 중복을 허용하지 않는다.

text1 = set("asdfasdf")
print("text1 : ", text1)

numbers = {2, 4, 5, 1, 2}
if 1 in numbers:  # numbers 속에 1이 있는가?
    print("집합에 1 이 있습니다.")

# 집합은 순서가 없어서 index로 접근이 불가능하다.
# 반복문으로 접근하여 출력 가능하다.
numbers = {9, 1, 2, 3, 6, 4, 4, 8, 5}
for num in numbers:
    print(num, end=" ")

print()

# 정렬 후 출력하기
for num in sorted(numbers):
    print(num, end=" ")

print()

# 추가하기
numbers.add(100)
print(numbers)
for num in sorted(numbers):
    print(num, end=" ")

print()

# 삭제하기

numbers.remove(100)
print(numbers)
