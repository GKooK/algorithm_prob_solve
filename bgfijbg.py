seat_count = 9
vip_seat_array = [4, 7]
import heapq

dp = [[1,0]]
def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    count = 1
    index = 1
    temp_adder = 0
    result_list = []
    while(index <= total_count):
        if index not in fixed_seat_array:
            temp_adder += 1
            index += 1
        else:
            index += 1
            #print(temp_adder)
            heapq.heappush(result_list, temp_adder*-1)
            #result_list.append(temp_adder)
            temp_adder = 0
    heapq.heappush(result_list, temp_adder*-1)
    for i in range(len(result_list)):
        temp=heapq.heappop(result_list)*-1
        if(i == 0):
            for k in range(temp):
                dp.append([dp[k][0]*2-dp[k][1], dp[k][0]-dp[k][1]])
        count *= dp[temp-1][0]

    return count


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))