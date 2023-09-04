def solution(survey, choices):
    answer = ''
    score = [[0,0] for _ in range(4)]
    survey_board = ["RT", "TR", "CF", "FC", "JM", "MJ", "AN", "NA"]
    
    # RT, FC, MJ, AN
    
    for i, sur in enumerate(survey):
        index = survey_board.index(sur)
        
        metric_category_id = index // 2 # 0,0, 1,1, 2,2, 3,3
        agree_side = index % 2 # 0이면 원래 순서, 1이면 반대 순서
        abs_score = abs(choices[i]-4)
        
        if agree_side == 1: # 1-> score[][1] += 3 / 2-> score[][1] += 2 / 3-> score[][1] += 1
            if choices[i] < 4:
                score[metric_category_id][1] += abs_score
            
            elif choices[i] > 4: 
                score[metric_category_id][0] += abs_score
        else:
            if choices[i] < 4:
                score[metric_category_id][0] += abs_score
            elif choices[i] > 4: 
                score[metric_category_id][1] += abs_score
        print(score)
            

    char_list = [["R", "T"], ["C","F"], ["J","M"], ["A","N"]]
    for char_id, check in enumerate(score):
        if check[0] >= check[1]:
            # 앞 글자 추가
            answer += char_list[char_id][0]
        else:
            #뒷 글자 추가
            answer += char_list[char_id][1]
        
    return answer