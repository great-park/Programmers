from itertools import permutations

def solution(k, dungeons):
    answer = 0 
    per_list = []
    
    for i in range(1, len(dungeons) + 1):
        per_list += list(permutations(dungeons, i))
        
    for schedule in per_list:
        cur_k, count = k, 0
        for s in schedule:
            min_need, cost = s[0], s[1]
            if cur_k < min_need:
                continue
            else:
                cur_k -= cost
                count += 1
        answer = max(answer, count)
    return answer
        