from collections import deque

def make_wires(wires, remove_id, n):
    graph = [[] for _ in range(n+1)]
    for id, wire in enumerate(wires):
        if id == remove_id:
            continue
        else:
            graph[wire[0]].append(wire[1])
            graph[wire[1]].append(wire[0])
    return graph
    
def BFS(start, graph, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    cnt = 1
    
    while q:
        x = q.popleft()
        for neighbor in graph[x]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True
                cnt += 1
    return cnt

def solution(n, wires):
    answer = []
    for i in range(len(wires)):
        graph = make_wires(wires, i, n)
        
        result = []
        visited = [False]*(n+1)
        for i in range(1,n+1):
            if not visited[i]:
                temp = BFS(i, graph, visited)
                result.append(temp)
        answer.append(abs(result[0]-result[1]))
        
    return min(answer)
        
    