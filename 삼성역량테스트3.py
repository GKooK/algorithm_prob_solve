import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]

def get_min_city_chicken_distance(n, m, city_map):
    chicken_house_location = []
    house_num = 0
    for i in range(n):
        for k in range(n):
            if(city_map[i][k] == 2):
                chicken_house_location.append([i,k])
            elif(city_map[i][k] == 1):
                house_num = house_num + 1
    hous_min = [32501]*house_num
    combintaion = list(itertools.combinations(chicken_house_location, m))
    return_val = 32501
    for i in combintaion:#각각의 조합들
        sum_of_distance = 0
        for j in range(n):
            for k in range(n):
                if(city_map[j][k] == 1):##각각의 집들에 대해서
                    temp = 32501
                    for l in i:#치킨집들과의 최솟값을 구해서 가장 짧은 치킨집을 구한 후 
                        temp = min(temp, (abs(l[0]-j)+abs(l[1]-k)))
                    sum_of_distance += temp#결과에 더해준다.
        return_val = min(return_val, sum_of_distance)

    return return_val

# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!