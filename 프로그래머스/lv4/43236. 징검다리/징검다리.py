def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    start, end = 0, distance
    
    while start <= end:
        mid = (start+end)//2 
        remove = 0
        current = 0
        min_distance = 1000000001
        for rock in rocks:
            distance = rock - current
            if distance < mid:
                remove+=1
                continue
            else:
                current = rock
                min_distance = min(min_distance, distance)
                
        if remove <= n:
            start = mid + 1
            answer = min_distance
        else:
            end = mid - 1
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