"""
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : 8.1 키와 값을 가지는 딕셔너리

    튜플 = () 리스트 = [] 딕셔너리 = {}
"""
# 빈 딕셔너리 생성
phone_book1 = {}

# 딕셔너리에 값 저장. key, value [key] = value
phone_book1["김현탁"] = "010-9660-1510"

print("phone_book1 :", phone_book1)  # {"김현탁" : "010-9660-1510"}

# 딕셔너리에 값 저장. 2. {key : value}
phone_book2 = {"홍길동": "010-7899-4545", "김현탁": "010-9660-1510"}
print("phone_book2 :", phone_book2)

phone_book3 = {}
phone_book3["김현탁"] = "010-9660-1510"
phone_book3["홍길동"] = "010-5656-7878"
phone_book3["정근우"] = "010-3265-6678"
phone_book3["이대호"] = "010-8945-7234"
phone_book3["신재영"] = "010-1134-3678"

print("phone_book3 : ", phone_book3)


print()
print(":: 전화번호 phone_book3 출력 ::")
# 모든 key 출력
print(phone_book3.keys())
# 모든 value 출력
print(phone_book3.values())
# 모든 key,value 출력
print(phone_book3.items())

print()

print(":: 전화번호 phone_book3 items() 출력 ::")
for name, phone_num in phone_book3.items():
    print(name, ":", phone_num)

print()

print(":: 전화번호 phone_book3 [keys]로 접근하여 출력 ::")
for key in phone_book3.keys():
    print(key, ":", phone_book3[key])

print()

print("딕셔너리 작성 시 :(콜론)을 기준으로 key 와 value 작성")
person_dict = {"name": "김현탁", "age": 24, "class": "1학년"}

print("name :", person_dict["name"])  # 딕셔너리의 'name' 키로 값을 조회하여 출력
print("age :", person_dict["age"])  # 딕셔너리의 'age' 키로 값을 조회하여 출력

print()

print(":: 정렬 ::")
# phone_book3 를 정렬
# 딕셔너리 키를 기준으로 정렬하여 리스트로 반환.
print(sorted(phone_book3))

print(":: 키를 기준으로 전체 정렬 ::")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x: x[0])
print(sort_phone_book3)

print(":: 값을 기준으로 전체 정렬 ::")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x: x[1])
print(sort_phone_book3)

print()

print(":: 항복 삭제 ::")
del phone_book3["김현탁"]
print(phone_book3)

print(":: 전체 삭제 ::")
phone_book3.clear()
print(phone_book3)
