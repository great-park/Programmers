def solution(distance, rocks, n):
    answer = 0
    left, right = 0, distance
    rocks.append(distance) # 마지막 도착지까지 거리를 계산하기 위해 추가
    rocks.sort() # 오름차순 정렬
    
    # 이분 탐색 수행
    while left <= right:
        mid = (left + right) // 2 # 특정한 최소거리
        current, remove =  0, 0 # 현재 위치, 제거할 바위 수
        min_distance = float('inf') # mid에서 최소 거리
        
        # 거리 구하기
        for rock in rocks:
            dis = rock - current
            if dis < mid: # mid 보다 작으면 바위 제거
                remove += 1
            else: # mid 보다 작지 않다면 현재 위치 옮기고 mi에서 최소 거리 계산
                current = rock
                min_distance = min(min_distance, dis)
                
        if remove > n: # n보다 많다면 mid를 줄임
            right = mid - 1
        else: # n보다 많지 않다면 최소 거리를 answer에 저장하고 mid를 늘림
            answer = min_distance
            left = mid + 1
        
    return answer