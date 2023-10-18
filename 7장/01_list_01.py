"""
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : 리스트 만들기
"""
# 과일 리스트 만들기
fruites = ["사과", "배", "딸기"]
print("과일 목록 : ", fruites)

# 수박 추가 => append() 메소드 사용 (마지막에 추가 ==> 우측 끝)
fruites.append("수박")
print("과일 목록(수박 추가) : ", fruites)

fruites.append("망고")
print("과일 목록(망고 추가) : ", fruites)


# 포도 추가 => + 연산자 사용 : 연결 연산자.
fruites = fruites + ["포도"]  # 포도를 더해서 fruites 에 저장  num = num + 1 과 같은 의미이다
print("과일 목록(포도 추가) : ", fruites)

num = [1, 2, 3] + [4, 5, 6]  # ==> 리스트에서 + 는 연결이다.
print("숫자 리스트 : ", num)  #   ==> [1,2,3,4,5,6]

# * 연산자 => 리스트를 n번 반복한다.
num = [1, 2, 3] * 3  # * 는 반복 횟수를 의미
print("숫자 리스트 * 3 : ", num)

# in 연산자 => 포함되는가?
print("과일 목록에 망고가 있나요? ", "망고" in fruites)

""""
    인덱스를 사용하여 리스트의 항목에 접근하기 178p
"""

# 과일 리스트에 있는 과일의 갯수는?
print("과일 리스트에 있는 과일의 갯수 : ", len(fruites))

# 과일 리스트 중 제일 첫 번째 과일은?
print("과일 중 제일 좋아하는 과일은? ", fruites[0])

# 과일 리스트 중 제일 마지막 과일은?
print("과일 중 제일 좋아하는 과일은? ", fruites[-1])

# 과일 중 가장 큰 과일은?
print("과일 중 제일 큰 과일은?(사전식 순서) ", max(fruites))

# 과일 중 가장 작은 과일은?
print("과일 중 제일 작은 과일은?(사전식 순서) ", min(fruites))

# 정렬
fruites.sort()  # 오름차순
print("오름차순 장렬 : ", fruites)
fruites.sort(reverse=True)  # 내림차순
print("내림차순 장렬 : ", fruites)

"""
    리스트를 원하는 모양으로 자르는 슬라이싱
"""
print("과일 목록 : ", fruites)
print("과일 리스트 중 2,3,4번 과일은? ", fruites[1:4])  # 1번지 ~ 4번지 앞까지
print("과일 리스트 중 1~3번 과일은? ", fruites[0:3])  # 0~2번지
print("과일 리스트 중 1~3번 과일은? ", fruites[:3])  # 처음부터 2번지까지
print("과일 리스트 중 3번 과일부터 마지막까지 과일은? ", fruites[2:])  # 3번부터 마지막까지
# 처음부터 끝까지 리스트 중에서 2씩 증가하면서.
print("과일 리스트 중 1,3,5번 과일은? ", fruites[::2])
print("과일 을 거꾸로 출력 ", fruites[::-1])

"""
    리스트의 원소 값을 자유롭게 조작해 보자.
"""
print()
print("과일 목록 : ", fruites)

# 원하는 위치에 '두리안' 추가 => insert() 메소드
fruites.insert(3, "두리안")
print("과일 목록(3번지에 두리안 추가) : ", fruites)

# 위치 찾기 =>index()메소드
print("사과의 위치는? ", fruites.index("사과"))

# 사과를 마지막에 추가
fruites.append("사과")
print("과일 목록(마지막에 사과 추가) : ", fruites)

# 사과의 개수 => count()메소드
print("사과의 개수는? ", fruites.count("사과"))

"""
    리스트의 항목 삭제
"""
print()

# 사과 삭제 => remove() 메소드 사용 : 삭제할 항목 지정.
fruites.remove("사과")  # 처음 만나는 사과만 삭제
print("과일 목록(사과 삭제 후) : ", fruites)

# 항목 삭제 => pop() 메소드
fruites.pop()  # 마지막 항목 삭제
print("과일 목록 (pop 후) : ", fruites)

# del() 키워드 => 포도 삭제
del fruites[0]  # 0번지 항목 삭제
print("과일 목록(포도[0번지] 삭제) : ", fruites)
