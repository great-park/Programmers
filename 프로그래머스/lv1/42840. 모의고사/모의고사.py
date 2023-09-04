def solution(answers):
    answer = []
    
    a,b,c = 0,0,0
    a_list = [1, 2, 3, 4, 5]
    b_list = [2, 1, 2, 3, 2, 4, 2, 5]
    c_list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a_size = 5
    b_size = 8
    c_size = 10
    
    for i, ans in enumerate(answers):
        # print(ans, a_list[(i)%a_size], b_list[(i)%b_size], c_list[(i)%c_size])
        if ans == a_list[i%a_size]:
            a += 1
        if ans == b_list[i%b_size]:
            b += 1
        if ans == c_list[i%c_size]:
            c += 1
    result = [a,b,c]
    max_num = max(result)
    for id, num in enumerate(result):
        if max_num == num:
            answer.append(id+1)
    answer.sort()
    return answer