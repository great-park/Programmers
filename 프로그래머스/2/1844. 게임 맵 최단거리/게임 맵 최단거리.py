from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# def solution(maps):
#     answer = 0
#     n, m = len(maps), len(maps[0])
#     visited = [[0]*m for _ in range(n)]
#     queue = deque()
#     queue.append([0,0])
#     visited[0][0] = 1
    
#     while queue:
#         x,y = queue.popleft()
        
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if 0<=nx<m and 0<=ny<n and visited[ny][nx] == 0:
#                 if maps[ny][nx] == 1:
#                     queue.append([nx,ny])
#                     visited[ny][nx] = visited[y][x] + 1

                        
#     if visited[n-1][m-1] != 0:
#         return visited[n-1][m-1]
#     else:
#         return -1

def solution(maps):
    n,m = len(maps), len(maps[0])
    visited = [[0]*m for _ in range(n)]
    queue = deque([(0,0)])
    visited[0][0] = 1
    
    while queue:
        x,y = queue.popleft()
        print(x,y)
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if 0<= nx < m and 0 <= ny < n and visited[ny][nx] == 0 and maps[ny][nx] == 1:
                queue.append([nx,ny])
                visited[ny][nx] = visited[y][x] + 1
                
    if visited[n-1][m-1] != 0:
        return visited[n-1][m-1]
    else:
        return -1
    
    