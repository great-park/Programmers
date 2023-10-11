from collections import deque


def main(M, N, K):
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    visited = [[False for _ in range(M)] for _ in range(N)]
    dx, dy = [1,0,-1,0], [0,1,0,-1]

    def BFS(x, y):
        q = deque()
        q.append([x, y])
        visited[y][x] = True
        while q:
            cur_node = q.popleft()
            x, y = cur_node[0], cur_node[1]

            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<M and 0<=ny<N and not visited[ny][nx] and graph[ny][nx] == 1:
                    q.append([nx,ny])
                    visited[ny][nx] = True
    count = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 1:
                BFS(j, i)
                count += 1
    print(count)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    main(M, N, K)
