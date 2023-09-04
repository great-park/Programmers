from collections import deque

def solution(queue1, queue2):
    answer = -2
    queue_a, queue_b = deque(queue1), deque(queue2)
    a_sum, b_sum = sum(queue_a), sum(queue_b)
    
    cnt = 0
    while True:
        if a_sum < b_sum: #b에서 a로 옮긴다.
            number = queue_b.popleft()
            queue_a.append(number)
            a_sum, b_sum = a_sum+number, b_sum-number
            cnt+=1
        elif a_sum > b_sum: #a에서 b로 옮긴다.
            number = queue_a.popleft()
            queue_b.append(number)
            a_sum, b_sum = a_sum-number, b_sum+number
            cnt+=1
        else:
            answer = cnt
            break
        
        if cnt > 6000001:
            answer = -1
            break
        
    return answer