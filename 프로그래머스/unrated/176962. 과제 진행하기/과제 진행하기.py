from collections import deque

def solution(plans):
    answer = []
    for i in range(len(plans)):
        hour, min = map(int, plans[i][1].split(":"))
        plans[i][1] = hour*60 + min
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x : x[1])
    
    print(plans)
    
    stack = []
    stack.append(plans[0])
    cur_time = plans[0][1]
    
    for i in range(1, len(plans)):
        next_time = plans[i][1]
        
        while stack:
            job, time_start, time_spend = stack.pop()
            
            if cur_time < time_start:
                cur_time = time_start
                
            time_finish = cur_time + time_spend
            
            if next_time < time_finish:
                 # 다음 작업을 스택에 넣을 때 까지는 시간 소모
                stack.append([job, time_start, time_finish - next_time])
                cur_time = next_time
                break
                
            else:
                answer.append(job)
                cur_time = time_finish
        
        stack.append(plans[i])
        
    while stack:
        answer.append(stack.pop()[0])
    
    
    return answer