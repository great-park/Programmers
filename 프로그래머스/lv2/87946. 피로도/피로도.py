from itertools import permutations

def solution(k, dungeons):
    answer = 0
    size = len(dungeons)
    
    for i in range(1, size+1):
        for nums in permutations(dungeons, i):
            temp_k = k
            temp_cnt = 0
            success = True
            for num in nums:
                if num[0] <= temp_k and temp_k >= num[1]:
                    temp_k -= num[1]
                else:
                    success = False
            if success:
                answer = len(nums)
    
    
    return answer