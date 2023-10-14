from itertools import permutations
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num+1):
        flag = num%i
        if flag == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = list(map(int, list(numbers)))
    permutation_num = []
    
    for i in range(1, len(nums)+1):
        permutation_num += permutations(nums, i)
    
    for p_num in permutation_num:
        for n in p_num:
            print(n)
    
    
    