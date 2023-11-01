"""
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자
"""
# 다음과 같은 리스트가 생성되어 있다.
city_info = [("서울", 9765), ("부산", 3441), ("인천", 2954), ("광주", 1501), ("대전", 1531)]

max_populater = city_info[0][1]  # 첫번째 항목이 기준.
min_populater = city_info[0][1]
total_pop = 0  # 총합 인원

max_city = city_info[0][0]  # 첫번째 항목이 기준.
min_city = city_info[0][0]

for city, populater in city_info:  # city 에 city info 를 넣고
    total_pop += populater  # city [1]은 인구수이므로 총합 인구수를 계산하기위해 합산함
    if populater > max_populater:  # city [1] 이 max_pop(최대인구수) 보다 클 경우 동작
        max_populater = city[1]  # max_pop(최대인구수를) city[1]에 인구수로 변경하고
        max_city = city  # max_city 를 현재 도시로 변경함
    if populater < min_populater:  # min_pop 는 최소 인구수이므로 현재 최소 인구수인 min_pop 보다 작을경우 동작함
        min_populater = city[1]  # min_pop 을 새로 갱신해주고
        min_city = city  # min_city 를 현재 도시로 변경함

print(
    "최대인구 : {0}, 인구 {1} 천명".format(max_city[0], max_populater)
)  # 가장 인구수가 많은 도시 이름[0번] 인구수[1번]를 출력함
print(
    "최대인구 : {0}, 인구 {1} 천명".format(min_city[0], min_populater)
)  # 가장 인구수가 적은 도시 이름[0번] 인구수[1번]를 출력함
print(
    "리스트 도시 평균 인수 : {0} 천명".format(total_pop / len(city_info))
)  # total pop(인구총합)/len(city_info) == 도시의 갯수 로 나누면 평균
