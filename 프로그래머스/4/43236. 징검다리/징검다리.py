def solution(distance, rocks, n):
    left = 1
    right = distance
    rocks.sort()
    rocks.append(distance)
    
    while left <= right:
        mid = (left+right)//2 # 돌 사이 거리의 최솟값
        remove = 0
        prev_rock = 0
        for rock in rocks:
            dist = rock - prev_rock
            
            if dist < mid:
                remove += 1
                if remove > n:
                    break
            else:
                prev_rock = rock
        if remove > n:
            right = mid -1
        else:
            answer = mid
            left = mid + 1
            
    return answer
                

    



# def solution(distance, rocks, n):
#     answer = 0
#     rocks.append(distance)
#     rocks.sort()
#     start, end = 0, distance
    
#     while start <= end:
#         mid = (start+end)//2
#         current, remove = 0,0
#         min_distance = 1000000001
#         for rock in rocks:
#             distance = rock - current
#             if distance < mid:
#                 remove += 1
#                 continue
#             else:
#                 current = rock
#                 min_distance = min(min_distance, distance)
        
#         if remove <= n:
#             start = mid + 1
#             answer = min_distance
#         else:
#             end = mid - 1
    
    
#     return answer 