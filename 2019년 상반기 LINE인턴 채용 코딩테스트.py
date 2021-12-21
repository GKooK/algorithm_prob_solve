from collections import deque
import math

c = 11
b = 2

#시간 t초
#cony_loc = cony loc + t*(t+1)/2
#brown_loc = brown_loc - t ~ brown_loc*(2**t)
#종료조건 if(cony_loc > 200,000)
def catch_me(cony_loc, brown_loc):
    first_cony_loc = cony_loc
    time = 0
    temp_area = [brown_loc]
    #temp_area = set()
    #temp_area.add(brown_loc)
    while(1):
        time = time +1
        #while(len(temp_area) == 0): #temp_area  에 값들 넣기
        for i in range(len(temp_area)):
            if((temp_area[0]-1) >= 0):
                if((temp_area[0]-1) not in temp_area):
                    temp_area.append(temp_area[0]-1)
            if((temp_area[0]+1) <= 200000):
                if((temp_area[0]+1) not in temp_area):
                    temp_area.append(temp_area[0]+1)
            if((temp_area[0]*2) <= 200000):
                if((temp_area[0]*2) not in temp_area):
                    temp_area.append(temp_area[0]*2)
            del temp_area[0] #큐에서 값 제거
        cony_loc = first_cony_loc + time*(time+1)//2
        if( cony_loc in temp_area):
            return time


#print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))