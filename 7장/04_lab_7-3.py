"""
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : 도시의 인구 자료에 대한 슬라이싱하기.
"""
population = ["Seoul", 9765, "Busan", 3441, "Incheon", 2954]
print("서울 인구: ", population[1])  # 리스트의 두번째
print("인천 인구: ", population[-1])  # 리스트의 뒤에서 첫번쨰
print("도시 리스트: ", population[::2])  # 1,3,5 .... 도시의 이름 출력
print("인구의 합: ", sum(population[1::2]))  # 도시의 인구를 합해줌 2,4,6 

