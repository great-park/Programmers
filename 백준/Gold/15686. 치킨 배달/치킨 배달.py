from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 1은 집, 2는 치킨집
homes = []
chickens = []
# 추가한 치킨집
ans = []
# 방문 목록
visited = [[0]*N for _ in range(N)]
# 거리 목록
distance_list = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            homes.append((i, j))
        elif graph[i][j] == 2:
            chickens.append((i, j))


def getDistance():
    x = 0
    # 집을 기준으로 치킨 거리를 계산. 한 집에 대해 여러 개의 치킨집 거리 계산
    for hx, hy in homes:
        distance = 1e9
        for id, (cx, cy) in ans:
            distance = min(distance, abs(hx-cx)+abs(hy-cy))
        x += distance
    distance_list.append(x)


# 치킨집을 하나씩 추가하면서 M개가 되었을 때 추가
def solve(depth):
    if depth == M:
        getDistance()
        return

    for id, (cx, cy) in enumerate(chickens):
        if not visited[cx][cy]:
            if ans:
                if id < ans[-1][0]:
                    continue
            visited[cx][cy] = 1
            ans.append((id, (cx, cy)))
            solve(depth+1)
            visited[cx][cy] = 0
            ans.pop()


solve(0)
print(min(distance_list))

# 백트래킹을 사용하면 더 효율적으로 개선할 수 있을 듯

# N, M = map(int, input().split())
# graph = []
# dx, dy = [1,0,-1,0], [0,1,0,-1]
# home_cordinate = []
# chicken_cordinate = []
# answer = 999999999
#
# for i in range(N):
#     sub_list = list(map(int, input().split()))
#     for j in range(N):
#         if sub_list[j] == 1:
#             home_cordinate.append([i,j])
#         elif sub_list[j] == 2:
#             chicken_cordinate.append([i,j])
#     graph.append(sub_list)
# def calculate(x1,y1,x2,y2):
#     return abs(x1-x2) + abs(y1-y2)
#
# def combi(arr, depth):
#     result = []
#
#     if depth == 0:
#         return [[]]
#
#     for i in range(0,len(arr)):
#         elem = arr[i]
#         rest_arr = arr[i+1:]
#         for c in combi(rest_arr, depth-1):
#             result.append([elem]+c)
#     return result
#
# def combination(array, r):
#     for i in range(len(array)):
#         if r == 1: # 종료 조건
#             yield [array[i]]
#         else:
#             for next in combination(array[i+1:], r-1):
#                 yield [array[i]] + next
#
# for i in range(1, M+1):
#     for chicken_list in combination(chicken_cordinate, i):
#         total_dist = 0
#         for home in home_cordinate:
#             dist_list = []
#             for chicken in chicken_list:
#                 dist = calculate(home[0], home[1], chicken[0], chicken[1])
#                 dist_list.append(dist)
#             total_dist += min(dist_list)
#
#         answer = min(total_dist, answer)
#
# print(answer)