# from collections import deque

# def BFS(cnum, visited, n, computers):
#     queue = deque()
#     queue.append(cnum)
#     visited[cnum] = True
    
#     while queue:
#         num = queue.popleft()
#         for i in range(n):
#             if i != num and computers[num][i] == 1 and not visited[i]:
#                 visited[i] = True
#                 queue.append(i)
#     return 
        
    

# def solution(n, computers):
#     answer = 0
#     visited = [False for _ in range(n)]
#     for cnum in range(n):
#         if not visited[cnum]:
#             BFS(cnum, visited, n, computers)
#             answer += 1
    
#     return answer

from collections import deque

def BFS(start_id, visited, computers, n):
    queue = deque()
    queue.append(start_id)
    visited[start_id] = True
    
    while queue:
        new_id = queue.popleft()
        for i in range(n):
            if not visited[i] and computers[new_id][i] == 1 and i != new_id:
                visited[i] = True
                queue.append(i)
    return

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for id in range(n):
        if not visited[id]:
            BFS(id, visited, computers, n)
            answer += 1
    return answer

