from itertools import permutations

def solution(k, dungeons):
    answer = 0
    per_list = []
    for i in range(1, len(dungeons)+1):
        per_list += list(permutations(dungeons))
    
    for schedule in per_list:
        tmp_k, tmp_answer = k, 0
        for dungeon in schedule:
            min_need, cost = dungeon[0], dungeon[1]
            if min_need > tmp_k:
                break
            else:
                tmp_k -= cost
                tmp_answer += 1
        answer = max(answer, tmp_answer)

    return answer










# from itertools import permutations

# def solution(k, dungeons):
#     answer = 0
#     size = len(dungeons)
    
#     for i in range(1, size+1):
#         for nums in permutations(dungeons, i):
#             temp_k = k
#             temp_cnt = 0
#             success = True
#             for num in nums:
#                 if num[0] <= temp_k and temp_k >= num[1]:
#                     temp_k -= num[1]
#                 else:
#                     success = False
#             if success:
#                 answer = len(nums)
    
    
#     return answer