from collections import deque
dx,dy=[0,0,1,-1], [1,-1,0,0]

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAX = 102
    graph = [[5]*MAX for _ in range(MAX)]
    for r in rectangle:
        x1,y1,x2,y2 = map(lambda x:x*2, r)
        
        for x in range(x1, x2+1):
            for y in range(y1,y2+1):
                if x1 < x < x2 and y1 < y < y2:
                    graph[x][y] = 0
                elif graph[x][y] != 0:
                    graph[x][y] = 1
                
    q = deque()
    visited = [[-1]*MAX for _ in range(MAX)]
    q.append([characterX*2, characterY*2])
    visited[characterX*2][characterY*2] = 1
    
    while q:
        cx, cy = q.popleft()
        if cx == itemX*2 and cy == itemY*2:
            answer = visited[cx][cy] // 2
            break
        
        for i in range(4):
            nx, ny = cx+dx[i], cy+dy[i]
            if visited[nx][ny] == -1 and graph[nx][ny] == 1:
                q.append([nx,ny])
                visited[nx][ny] = visited[cx][cy] + 1
    return answer


