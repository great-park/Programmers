N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N

min_value = 1e9

def solve():
    global min_value
    s_result = 0
    l_result = 0

    s_list = [id for id, is_s in enumerate(visited) if is_s]
    l_list = [id for id, is_s in enumerate(visited) if not is_s]

    for i in range(N//2):
        for j in range(i+1, N//2):
            s1, s2 = s_list[i], s_list[j]
            l1, l2 = l_list[i], l_list[j]
            s_result += ab[s1][s2] + ab[s2][s1]
            l_result += ab[l1][l2] + ab[l2][l1]

    min_value = min(min_value, abs(s_result - l_result))


def DFS(depth, id):
    if depth == N // 2:
        solve()
        return
    else:
        for i in range(id, N):
            if not visited[i]:
                visited[i] = True
                DFS(depth+1, i)
                visited[i] = False


DFS(0,1)
print(min_value)




# from itertools import combinations
#
# import sys
# N = int(sys.stdin.readline())
# stat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# player = [False for _ in range(N)]
# minValue = N//2 * (N//2-1) * 100
#
#
# def get_ans():
#     global minValue
#     s_result = 0
#     l_result = 0
#     # enumerate -> 인덱스와 요소를 튜플로 반복
#     sTeam = [idx for idx, val in enumerate(player) if val == True]
#     lTeam = [idx for idx, val in enumerate(player) if val == False]
#     for i in range(0, N//2):
#         for j in range(i+1, N//2):
#             s_first = sTeam[i]
#             s_second = sTeam[j]
#             s_result += stat[s_first][s_second] + stat[s_second][s_first]
#
#             l_first = lTeam[i]
#             l_second = lTeam[j]
#             l_result += stat[l_first][l_second] + stat[l_second][l_first]
#
#     minValue = min(minValue, abs(s_result - l_result))
#
#
# def dfs(depth, idx):
#     if depth == N/2:
#         get_ans()
#         return
#     for i in range(idx, N):
#         if player[i]:
#             continue
#
#         player[i] = True
#         dfs(depth+1, i)
#         player[i] = False  # 백트래킹
#
#
# dfs(0, 1)
# print(minValue)


"""
"""
#
# n = int(input())
# arr = []
# v = []
# ans = 1e9
# # 전체팀을 집합으로 구해놓는게 시간상 더 쉽게 구할수 있습니다.
# total_team = set(range(0, n))
# c_range = [x for x in range(n)]
# for _ in range(n):
#     arr.append(list(map(int, input().split())))
#
# for team_a in combinations(c_range, n//2):
#     # 그리고 team_b는 tuple로 하는 것보다 집합의 차집합을 통해 쉽게 구할수 있습니다.
#     team_b = list(total_team - set(team_a))
#     sum_a = 0
#     sum_b = 0
#     # 여기서 시간을 많이 나간것 같습니다.
#     # combination 대신 직접 range를 돌리면서 하는게 더 빠를 것 같습니다.
#     for index_a in range(n//2):
#         for index_b in range(index_a+1, n//2):
#             sum_a += arr[team_a[index_a]][team_a[index_b]] + \
#                 arr[team_a[index_b]][team_a[index_a]]
#             sum_b += arr[team_b[index_a]][team_b[index_b]] + \
#                 arr[team_b[index_b]][team_b[index_a]]
#     temp = abs(sum_a-sum_b)
#
#     if temp < ans:
#         ans = temp
# print(ans)
