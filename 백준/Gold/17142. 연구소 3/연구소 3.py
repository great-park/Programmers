# 드디어 성공
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



# 아래는 84프로 실패 버전 - graph를 직접 바꿔서 잘못되는 케이스가 생긴 듯

# from collections import deque
# import copy
#
# N, M = map(int, input().split())
# graph = []
# dx, dy = [1,0,-1,0], [0,1,0,-1]
# virus = []
# answer = 2147000000
#
# for i in range(N):
#     sub_list = list(map(int, input().split()))
#     for k in range(N):
#         if sub_list[k] == 2:
#             virus.append([k,i])
#             sub_list[k] = 0
#         elif sub_list[k] == 1:
#             sub_list[k] = -1 # 벽은 -1로 수정한다. 나중에 탐색 깊이를 graph에 저장할거임
#     graph.append(sub_list)
#
# def BFS(virus_list, graph_copy, active_virus_list):
#     q = deque()
#     visited = [[False for _ in range(N)] for _ in range(N)]
#     for v in virus_list:
#         x, y = v[0], v[1]
#         q.append([x, y])
#         visited[y][x] = True
#
#     while q:
#         cur_node = q.popleft()
#         cx, cy = cur_node[0], cur_node[1]
#         for i in range(4):
#             nx, ny = cx+dx[i], cy+dy[i]
#             if 0<=nx<N and 0<=ny<N and graph_copy[ny][nx] != -1 and not visited[ny][nx]:
#                 q.append([nx, ny])
#                 visited[ny][nx] = True
#                 if graph_copy[ny][nx] == -9: # 비활성 바이러스가 활성으로 변한다.
#                     graph_copy[ny][nx] = 0
#                     active_virus_list.append([nx,ny])
#                 else:
#                     graph_copy[ny][nx] = graph_copy[cy][cx] + 1
#     time = 0
#     for s in graph_copy:
#         for v in s:
#             time = max(time, v)
#     return time
#
# def combination(arr, depth):
#     for i in range(len(arr)):
#         if depth == 1:
#             yield [arr[i]]
#         else:
#             for next in combination(arr[i+1:], depth-1):
#                 yield [arr[i]] + next
#
# final_success = False
#
# for c in combination(virus, M):
#     graph_copy = copy.deepcopy(graph)
#     # 비활성화 바이러스는 마이너스 값으로 교체
#     for v in virus:
#         if v not in c:
#             graph_copy[v[1]][v[0]] = -9
#     active_virus_list = copy.deepcopy(c)
#     result_time = BFS(c, graph_copy, active_virus_list)
#     success = True
#
#     # 모두 감염되었는지 확인
#     for i in range(N):
#         for j in range(N):
#             if graph_copy[j][i] == 0 and [i,j] not in active_virus_list:
#                 success = False
#
#     if success:
#         answer = min(answer, result_time)
#         final_success = True
#
# # 모든 경우의 수에서 성공한 적이 없으면 최종적으로 -1이 정답이다.
# if not final_success:
#     answer = -1
#
# print(answer)
