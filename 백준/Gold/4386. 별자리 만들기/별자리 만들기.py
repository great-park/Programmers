import math

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x, y = find(x), find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n = int(input())
parent = [i for i in range(n+1)]
stars, edges, result = [], [], 0

for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x,y))

for i in range(n-1):
    for j in range(i+1, n):
        cost = math.sqrt((stars[i][0]-stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)
        edges.append((cost,i,j))
edges.sort(key=lambda x:x[0])

for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a,b)
        result += cost
print(round(result, 2))