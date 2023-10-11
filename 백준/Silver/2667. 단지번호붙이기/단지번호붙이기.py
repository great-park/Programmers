from collections import deque

N = int(input())
graph = []
result = []
for _ in range(N):
    graph.append(list(int(x) for x in input()))

visited = [[False for _ in range(N)] for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(x,y):
    count = 1
    q = deque()
    q.append([x,y])
    visited[y][x] = True

    while q:
        cur_node = q.popleft()
        x, y = cur_node[0], cur_node[1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and graph[ny][nx] != 0 and not visited[ny][nx]:
                q.append([nx,ny])
                visited[ny][nx] = True
                count += 1
    return count

for i in range(N):
    for j in range(N):
        if not visited[j][i] and graph[j][i] != 0:
            result.append(BFS(i,j))


print(len(result))
result.sort()
for v in result:
    print(v)    