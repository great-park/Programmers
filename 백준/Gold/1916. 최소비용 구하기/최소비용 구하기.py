import sys
import heapq

N=int(sys.stdin.readline().rstrip())
M=int(sys.stdin.readline().rstrip())

graph=[[] for _ in range(N+1)]

for i in range(M):
    a,b,c=map(int,sys.stdin.readline().rstrip().split())
    graph[a].append([b,c])

startpoint,endpoint=map(int,sys.stdin.readline().rstrip().split())

def dijkstra(start):
    d=[999999999 for _ in range(N+1)]
    d[start]=0
    que=[]
    heapq.heappush(que,(d[start],start))
    while que:
        dis,node=heapq.heappop(que)
        if d[node]<dis: #이미 노드에 대한 최단거리 존재시 과정 패스 
            continue
        for i in graph[node]: #node의 노드에서 거리비용 탐색
            gnode=i[0] #그래프에서 탐색당하는 노드
            gdis=i[1] #그래프에서 탐색당하는 노드의 거리비용
            updatedis=d[node]+gdis
            if updatedis<d[gnode]:
                d[gnode]=updatedis
                heapq.heappush(que,(d[gnode],gnode))
    return d

print(dijkstra(startpoint)[endpoint])