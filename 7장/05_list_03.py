"""
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : 리스트의 객체 생성과 참조
"""
fruites1 = ["딸기", "수박", "바나나"]

fruites2 = fruites1

print("Fruites1 : ", fruites1)
print("Fruites2 : ", fruites2)

# 실제 값을 복사하는 것이 아니라 리스트의 저장 위치(주소)가 복사된다. (같은곳을 참조한다)
fruites2[1] = "망고"  # fruites 2의 [1]번지 과일을 망고로 바꾸면..

print("Fruites1 : ", fruites1)  # 모두 1번지 내용이 망고로 바뀐다.
print("Fruites2 : ", fruites2)  # 주소를 참조하기 때문

# 주소 확인 => 메모리 정보 알아보기 id()함수
print("fruites1의 id : ", id(fruites1))
print("fruites2의 id : ", id(fruites2))  # 두 리스트의 id정보가 같다.

"""
    리스트 내용 복제하기 list()함수
"""

fruites2 = list(fruites1)  # 내용 복제(배정)
print(":: 내용 복제 후 1 ::")

print("fruites1 : ", fruites1)
print("fruites2 : ", fruites2)

print("fruites1의 id : ", id(fruites1))
print("fruites2의 id : ", id(fruites2))

# 내용 복제 2
fruites3 = fruites1[:]

print(":: 내용 복제 후 2 ::")

print("fruites1 : ", fruites1)
print("fruites3 : ", fruites3)

print("fruites1의 id : ", id(fruites1))  # id 정보가 다르다
print("fruites3의 id : ", id(fruites3))

fruites3[0] = "수박"  # 0번지 내용을 수박으로 바꾼다.
print(":: fruites3의 0번지를 수박으로 바꾼 후 ::")
print("fruites1 : ", fruites1)
print("fruites3 : ", fruites3)
