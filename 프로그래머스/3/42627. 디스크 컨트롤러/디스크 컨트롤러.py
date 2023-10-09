import heapq as hq
def solution(jobs):
    total_time, now, done = 0,0,0
    start = -1
    heap = []
    
    while done < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                hq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = hq.heappop(heap)
            start = now
            now += current[0]
            done += 1
            total_time += now - current[1]
        else:
            now += 1
    
    return total_time // len(jobs)