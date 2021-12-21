from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

#0은 위
#1은 왼쪽
#2는 아래
#3은 오른쪽,        R은 R좌표, B는 B좌표
def move_map(game_map, move_way, R, B):
    if(move_way%2 == 0):
        move_way = move_way-1
        while(1):
            if(game_map[R[0]+move_way][R[1]] == 'O'):
                return 1
            elif(game_map[R[0]+move_way][R[1]] == '#'):
                break
            elif(game_map[R[0]+move_way][R[1]] != 0):
                game_map[R[0]][R[1]], game_map[R[0]+move_way][R[1]] = game_map[R[0]+move_way][R[1]], game_map[R[0]][R[1]]
                R[0] = R[0] + move_way
    else:
        move_way = move_way - 2
        while(1):
            if(game_map[R[0]][R[1]+move_way] == 'O'):
                return 1
            elif(game_map[R[0]][R[1]+move_way] == '#'):
                break
            elif(game_map[R[0]][R[1]+move_way] != 0):
                game_map[R[0]][R[1]], game_map[R[0]][R[1]+move_way] = game_map[R[0]][R[1]+move_way], game_map[R[0]][R[1]]
                R[1] = R[1] + move_way
    return [game_map, R, B]

def is_available_to_take_out_only_red_marble(game_map):
    # 구현해보세요!
    r_location = []
    b_location = []
    for i in range(len(game_map)):
        for k in range(len(game_map)):
            if("R" == game_map[i][k]):
                r_location.append(i)
                r_location.append(k)
            if("B" == game_map[i][k]):
                b_location.append(i)
                b_location.append(k)
    bfs_queue = deque()
    bfs_queue.append([game_map, r_location, b_location])
    count = 0
    while((len(bfs_queue)!=0) and (count < 10)):
        count = count + 1
        temp_queue = deque()
        while(len(bfs_queue)!=0):
            temp_queue.append(bfs_queue.popleft())
        while(len(temp_queue) != 0):
            pop_value = temp_queue.popleft()
            for i in range(4):
                temp = move_map(pop_value[0], i, pop_value[1], pop_value[2])
                if(temp == 1):
                    return True
                elif(temp != 0):
                    bfs_queue.append(temp)
            
    return False

print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다
