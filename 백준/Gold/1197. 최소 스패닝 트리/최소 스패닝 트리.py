V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])
parent = [i for i in range(V+1)]

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)
    if a < b: 
        parent[b] = a
    else:
        parent[a] = b        
        
answer = 0
for a, b, cost in edges:
    if get_parent(a) != get_parent(b):
        union_parent(a, b)
        answer += cost
print(answer)