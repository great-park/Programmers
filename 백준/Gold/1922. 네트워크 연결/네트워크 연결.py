from sys import stdin
input = stdin.readline
N = int(input())
M = int(input())
graph = []
parent = [i for i in range(N+1)]


def find(a):
    if a == parent[a]:  # 자신이 루트노드면 자신을 반환한다.
        return a
    parent[a] = find(parent[a])

    return parent[a]  # a의 부모를 find(parent[a])로 변경


def union(a, b):
    a = find(a)
    b = find(b)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a


def solve(g):
    global res
    for distance, a, b in g:
        if find(a) != find(b):
            union(a, b)
            res += distance

    print(res)


res = 0
for i in range(M):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))
graph.sort(key=lambda x: x[0])
solve(graph)
