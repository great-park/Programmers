from collections import deque

def BFS(start_id, visited, computers):
    queue = deque()
    queue.append(start_id)
    visited[start_id] = True
    
    while queue:
        cur_id = queue.popleft()
        
        for new_id, value in enumerate(computers[cur_id]):
            if new_id != cur_id and not visited[new_id] and value == 1:
                queue.append(new_id)
                visited[new_id] = True
    
    

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for id in range(n):
        if not visited[id]:
            BFS(id, visited, computers)
            answer += 1
    return answer

