def solution(brown, yellow):
    answer = []
    total_block = brown+yellow
    
    for h in range(1, total_block+1):
        if total_block % h == 0:
            v = total_block // h
            
            if v < h:
                continue
            
            if yellow == (v-2)*(h-2):
                answer.extend([v,h])

    return answer


    
    
    
    
    



   
    
    
# def solution(brown, yellow):
#     answer = []
#     total = brown + yellow                  # a * b = total
#     for b in range(1,total+1):
#         if (total / b) % 1 == 0:            # total / b = a
#             a = total / b
#             if a >= b:                      # a >= b
#                 if 2*a + 2*b == brown + 4:  # 2*a + 2*b = brown + 4 
#                     return [a,b]
            
#     return answer