from collections import deque
import sys
N, M = map(int, input().split())
graph = []
dx, dy = [1,0,-1,0], [0,1,0,-1]
virus = []
inf = sys.maxsize
wall = 0
room = 0
for i in range(N):
    sub_list = list(map(int, input().split()))
    for k in range(N):
        if sub_list[k] == 2:
            virus.append([k,i])
        elif sub_list[k] == 1:
            wall+=1
        elif sub_list[k] == 0:
            room +=1
    graph.append(sub_list)

def BFS(active_virus):
    q = deque()
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    for v in active_virus:
        vx, vy = v[0], v[1]
        q.append([vx, vy])
        visited[vy][vx] = 0

    result = 0
    infect_place = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if graph[ny][nx] == 0 and visited[ny][nx] == -1:
                    q.append([nx,ny])
                    visited[ny][nx] = visited[y][x] + 1
                    result = max(result, visited[ny][nx])
                    infect_place += 1
                elif graph[ny][nx] == 2 and visited[ny][nx] == -1:
                    q.append([nx, ny])
                    visited[ny][nx] = visited[y][x] + 1

    if room == infect_place:
        if room == 0:
            return 0
        else:
            return result
    else:
        return inf




def combinations(arr, depth):
    for i in range(len(arr)):
        if depth == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], depth-1):
                yield [arr[i]] + next

answer = inf

for active_virus in combinations(virus, M):
    answer = min(answer, BFS(active_virus))

print(answer if answer != inf else -1)