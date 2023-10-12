from collections import deque

N, M = map(int, input().split())
graph = []
dx, dy = [1,0,-1,0], [0,1,0,-1]
home_cordinate = []
chicken_cordinate = []
answer = 999999999

for i in range(N):
    sub_list = list(map(int, input().split()))
    for j in range(N):
        if sub_list[j] == 1:
            home_cordinate.append([i,j])
        elif sub_list[j] == 2:
            chicken_cordinate.append([i,j])
    graph.append(sub_list)
def calculate(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

# 치킨 거리 계산 BFS
# 각 집에서 치킨 집까지의 치킨 거리를 계산한다. - 생각해보니 이러면 BFS 안 써도 될 듯
# def BFS(x,y):
#     q = deque()
#     visited = [[False for _ in range(N)] for _ in range(N)]
#     q.append([x,y])
#     visited[y][x] = True
#     dist_list = []
#
#     while q:
#         cur_node = q.popleft()
#         cx, cy = cur_node[0], cur_node[1]
#
#         for i in range(4):
#             nx, ny = cx+dx[i], cy+dy[i]
#             if 0<=nx<N and 0<=ny<N and not visited[ny][nx]:
#                 if graph[ny][nx] == 2:
#                     dist = calculate(x,y,nx,ny)
#                     dist_list.append(dist)
#                 q.append([nx, ny])
#                 visited[ny][nx] = True


# 최대 M개의 치킨집을 남기는 백트래킹

def combi(arr, depth):
    result = []

    if depth == 0:
        return [[]]

    for i in range(0,len(arr)):
        elem = arr[i]
        rest_arr = arr[i+1:]
        for c in combi(rest_arr, depth-1):
            result.append([elem]+c)
    return result

def combination(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combination(array[i+1:], r-1):
                yield [array[i]] + next

for i in range(1, M+1):
    for chicken_list in combination(chicken_cordinate, i):
        total_dist = 0
        for home in home_cordinate:
            dist_list = []
            for chicken in chicken_list:
                dist = calculate(home[0], home[1], chicken[0], chicken[1])
                dist_list.append(dist)
            total_dist += min(dist_list)

        answer = min(total_dist, answer)

print(answer)