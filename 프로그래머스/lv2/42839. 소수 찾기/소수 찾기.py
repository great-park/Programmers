from itertools import permutations

def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, number):
        flag = number%i
        if flag == 0:
            return False
    return True

def solution(numbers):
    answer = []
    nums = [n for n in numbers]
    per_list = []
    for i in range(1, len(nums)+1):
        per_list += list(permutations(nums, i))
        # print(per_list)
    number_list = list(set(int(("").join(p)) for p in per_list))
    
    for test_num in number_list:
        if is_prime(test_num):
            answer.append(test_num)
    
    return len(answer)