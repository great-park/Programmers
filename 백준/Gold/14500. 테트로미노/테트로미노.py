N, M = map(int, input().split())
graph = []
dx, dy = [1,0,-1,0], [0,1,0,-1]
max_val_in_graph = 0
for i in range(N):
    sub = list(map(int, input().split()))
    max_val_in_graph = max(max_val_in_graph, max(sub))
    graph.append(sub)

# 테트로미노를 하나 놓는다는 건, depth가 4인 dfs를 한 번 실시하는 것이다. 단 ㅗ 모양은 예외이다.

# depth = 1 일 때(즉, 두개의 블럭을 선택했을 때) 새로운 블럭에서 다음 블럭을 탐색하는 것이 아니라 다시 기존블럭에서 탐색하게 만들면 ㅗ모양을 만들 수 있다.

visited = [[False for _ in range(M)] for _ in range(N)]
answer = 0
def DFS(x,y, depth, sum):
    global answer
    if answer >= sum + max_val_in_graph * (3-depth):
        return
    if depth == 3:
        answer = max(answer, sum)
        return
    else:
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<M and 0<=ny<N and not visited[ny][nx]:
                if depth == 1:
                    visited[ny][nx] = True
                    DFS(x,y,depth+1,sum+graph[ny][nx]) # depth가 1이면 이전 노드를 다시 탐색해서 ㅗ 모양을 포함시킨다.
                    visited[ny][nx] = False
                visited[ny][nx] = True
                DFS(nx,ny,depth+1,sum+graph[ny][nx])
                visited[ny][nx] = False

for i in range(M):
    for j in range(N):
        visited[j][i] = True
        DFS(i,j,0,graph[j][i])
        visited[j][i] = False

print(answer)