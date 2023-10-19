from collections import deque

def BFS(i, visited, computers):
    visited[i] = True
    q = deque()
    q.append(i)
    
    while q:
        cur_id = q.popleft()
        for new_id, value in enumerate(computers[cur_id]):
            if new_id != cur_id and not visited[new_id] and value == 1:
                q.append(new_id)
                visited[new_id] = True
    
    

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if not visited[i]:
            BFS(i, visited, computers)
            answer += 1

    return answer

