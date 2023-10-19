from collections import deque

def solution(numbers, target):
    answer = 0
    size = len(numbers)
    q = deque()
    q.append([numbers[0], 1])
    q.append([-numbers[0], 1])
    
    while q:
        x, depth = q.popleft()
        
        if depth < size:
            q.append([x+numbers[depth], depth+1])
            q.append([x-numbers[depth], depth+1])
        else:
            if x == target:
                answer += 1
    
    
    return answer
        
    
















# from collections import deque
# def solution(numbers, target):
#     answer = 0
#     size = len(numbers)
#     queue = deque()
#     queue.append((numbers[0], 1))
#     queue.append((-numbers[0], 1))
    
#     while queue:
#         number, depth = queue.popleft()
#         depth += 1
#         if depth <= size:
#             queue.append((number+numbers[depth-1], depth))
#             queue.append((number-numbers[depth-1], depth))
#         else:
#             if number == target:
#                 answer += 1
    
    
#     return answer

