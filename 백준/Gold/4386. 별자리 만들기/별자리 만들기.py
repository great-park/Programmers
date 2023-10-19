"""
최소 스패닝 트리 유형 문제이다.
다른 문제와 달랐던 점은 간선의 거리 대신 별들의 좌표가 주어진다는 것이다.
따라서 간선들의 리스트를 만들기 위해 모든 별들 간의 거리를 계산해주어야 했다.
이후 일반적인 최소 스패닝 트리 유형처럼 간선들을 오름차순으로 정렬해준다.
그리고 간선과 연결된 두 노드의 부모를 비교하여 다를 경우에만 두 노드를 연결하는 과정(부모를 똑같게)을 거친다.
출력 시 소수 둘째자리까지 출력하도록 신경써준다.
"""
import math

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [i for i in range(n + 1)]

stars = []
edges = []
result = 0

for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

for i in range(n - 1):
    for j in range(i + 1, n):
        edges.append((math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), i, j))

edges.sort()

for edge in edges:
    cost, x, y = edge

    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        result += cost

print(round(result, 2))