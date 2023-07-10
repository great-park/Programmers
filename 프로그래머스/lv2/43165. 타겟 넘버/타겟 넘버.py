from collections import deque
def solution(numbers, target):
    answer = 0
    size = len(numbers)
    queue = deque()
    queue.append((numbers[0], 1))
    queue.append((-numbers[0], 1))
    
    while queue:
        number, depth = queue.popleft()
        depth += 1
        if depth <= size:
            queue.append((number+numbers[depth-1], depth))
            queue.append((number-numbers[depth-1], depth))
        else:
            if number == target:
                answer += 1
    
    
    return answer

