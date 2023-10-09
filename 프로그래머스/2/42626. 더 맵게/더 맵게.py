1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer

# import heapq

# def solution(scoville, K):
#     answer = 0
#     heap = []
#     for s in scoville:
#         heapq.heappush(heap, s)
    
#     while heap[0] < K:
#         heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap)*2)
#         answer+=1
    
#         if len(heap) == 1 and heap[0] < K:
#             answer = -1
#             break
    
#     return answer