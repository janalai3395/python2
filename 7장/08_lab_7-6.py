"""
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자
"""
# 다음과 같은 리스트가 생성되어 있다.
city_info = [("서울", 9765), ("부산", 3441), ("인천", 2954), ("광주", 1501), ("대전", 1531)]

max_pop = 0  # 최대인구수 (비교시에 갱신을 위해 0을 넣어줌)
min_pop = 999999  # 최소인구수 (비교시에 갱신을 위하여 최대 인구수보다 큰 값을 넣어줌)
total_pop = 0  # 총합 인원

max_city = None  # 가장인구가 많은 도시에 정보를 담을 변수
min_city = None  # 가장인구가 적은 도시에 정보를 담을 변수

for city in city_info:  # city 에 city info 를 넣고
    total_pop += city[1]  # city [1]은 인구수이므로 총합 인구수를 계산하기위해 합산함
    if city[1] > max_pop:  # city [1] 이 max_pop(최대인구수) 보다 클 경우 동작
        max_pop = city[1]  # max_pop(최대인구수를) city[1]에 인구수로 변경하고
        max_city = city  # max_city 를 현재 도시로 변경함
    if city[1] < min_pop:  # min_pop 는 최소 인구수이므로 현재 최소 인구수인 min_pop 보다 작을경우 동작함
        min_pop = city[1]  # min_pop 을 새로 갱신해주고
        min_city = city  # min_city 를 현재 도시로 변경함

print(
    "최대인구 : {0}, 인구 {1} 천명".format(max_city[0], max_city[1])
)  # 가장 인구수가 많은 도시 이름[0번] 인구수[1번]를 출력함
print(
    "최대인구 : {0}, 인구 {1} 천명".format(min_city[0], min_city[1])
)  # 가장 인구수가 적은 도시 이름[0번] 인구수[1번]를 출력함
print(
    "리스트 도시 평균 인수 : {0} 천명".format(total_pop / len(city_info))
)  # total pop(인구총합)/len(city_info) == 도시의 갯수 로 나누면 평균
