import sys

def find_set(x, parent):
    if x != parent[x]:
        parent[x] = find_set(parent[x], parent)
    return parent[x]

def union(x, y, parent, rank):
    x = find_set(x, parent)
    y = find_set(y, parent)
    if x == y:
        return False
    if rank[x] > rank[y]:
        parent[y] = x
    elif rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[x] = y
        rank[y] += 1
    return True

def kruskal(edges, n):
    parent = [i for i in range(n)]
    rank = [1] * n
    mst_cost = 0

    for cost, u, v in sorted(edges):
        if union(u, v, parent, rank):
            mst_cost += cost

    return mst_cost

def main():
    n = int(sys.stdin.readline())
    planets = [tuple(map(int, sys.stdin.readline().split())) + (i,) for i in range(n)]

    edges = []
    for dim in range(3):
        planets.sort(key=lambda x: x[dim])
        for i in range(1, n):
            cost = abs(planets[i - 1][dim] - planets[i][dim])
            u, v = planets[i - 1][3], planets[i][3]
            edges.append((cost, u, v))

    print(kruskal(edges, n))

if __name__ == "__main__":
    main()
