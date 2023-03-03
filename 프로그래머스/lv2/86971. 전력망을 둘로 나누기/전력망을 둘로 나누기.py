from collections import deque
from itertools import permutations

"""
BFS 함수 만들고, 완탐으로 하나씩 끊어보면서 개수 체크
"""
def BFS(graph,i,visited):
    queue = deque()
    queue.append(i)
    visited[i] = True
    cnt = 1
    while queue:
        x = queue.popleft()
        
        for adj in graph[x]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = True
                cnt += 1
    return cnt
    

def solution(n, wires):
    answer = []
    size = len(wires)
    for i in range(size):
        new_wires = []
        for j in range(size):
            if i == j:
                continue
            new_wires.append(wires[j])
            
        result = []
        graph = [[] for _ in range(n+1)]
        for d in new_wires:
            a,b = d[0], d[1]
            graph[a].append(b)
            graph[b].append(a)
        visited = [False]*(n+1)
        for i in range(1,n+1):
            if not visited[i]:
                result.append(BFS(graph,i,visited))
        answer.append(abs(result[0] - result[1]))
    
    return min(answer)