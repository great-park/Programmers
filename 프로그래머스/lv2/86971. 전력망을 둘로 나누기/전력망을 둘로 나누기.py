from collections import deque
from itertools import permutations


def make_graph(wires, n):
    graph = [[] for _ in range(n+1)]
    visited = [[False] for _ in range(n+1)]
    for wire in wires:
        x,y = wire[0], wire[1]
        graph[x].append(y)
        graph[y].append(x)
    return graph
        
def BFS(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    cnt = 1
    
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if not visited[y]:
                queue.append(y)
                visited[y] = True
                cnt += 1
    return cnt

def solution(n, wires):
    # 주어진 wires에서 한 edge씩 제거한 뒤 그래프 형성 후 BFS해서 카운트하기 -> 모아서 최댓값 구함
    answer = []
    for remove_id in range(len(wires)):
        n_wires = []
        for i in range(len(wires)):
            if i != remove_id:
                n_wires.append(wires[i])
        graph = make_graph(n_wires, n)
        visited = [False for _ in range(n+1)]
        result_cnt = 0
        result = []
        for i in range(1, n+1):
            if not visited[i]:
                result_cnt = BFS(graph, i, visited)
                result.append(result_cnt)
        answer.append(abs(result[0]-result[1]))

    return min(answer)
    
    








# from collections import deque
# from itertools import permutations

# """
# BFS 함수 만들고, 완탐으로 하나씩 끊어보면서 개수 체크
# """
# def BFS(graph,i,visited):
#     queue = deque()
#     queue.append(i)
#     visited[i] = True
#     cnt = 1
#     while queue:
#         x = queue.popleft()
        
#         for adj in graph[x]:
#             if not visited[adj]:
#                 queue.append(adj)
#                 visited[adj] = True
#                 cnt += 1
#     return cnt
    

# def solution(n, wires):
#     answer = []
#     size = len(wires)
#     for i in range(size):
#         new_wires = []
#         for j in range(size):
#             if i == j:
#                 continue
#             new_wires.append(wires[j])
            
#         result = []
#         graph = [[] for _ in range(n+1)]
#         for d in new_wires:
#             a,b = d[0], d[1]
#             graph[a].append(b)
#             graph[b].append(a)
#         visited = [False]*(n+1)
#         for i in range(1,n+1):
#             if not visited[i]:
#                 result.append(BFS(graph,i,visited))
#         answer.append(abs(result[0] - result[1]))
    
#     return min(answer)