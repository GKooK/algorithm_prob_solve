# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

def bfs_queue(adj_graph, start_node):
    # 구현해보세요!
    visited = []
    can_go = [start_node]
    while(len(can_go)!=0):
        queue_pop_one = can_go[0]
        del can_go[0]
        visited.append(queue_pop_one)
        for i in adj_graph[queue_pop_one]:
            if(i not in visited):
                can_go.append(i)
    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!