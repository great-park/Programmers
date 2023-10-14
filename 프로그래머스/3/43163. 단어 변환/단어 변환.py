from collections import deque

def solution(begin, target, words):
    answer = 0
    
    # begin부터 시작해서 글자가 하나만 다른 단어들을 큐에 넣는다. 
    # target과 같으면 탐색을 종료

    queue = deque()
    n = len(words)
    visited = [False]*n
    queue.append([begin, 0])
    success = False
    
    while queue:
        test, cnt = queue.popleft()
        test_list = list(test)
        if test == target:
            success = True
            answer = cnt
            break
    
        for i, word in enumerate(words):
            if visited[i]:
                continue
            
            diff_cnt = 0
            char_list = list(word)
            for id, char in enumerate(char_list):
                if test_list[id] != char:
                    diff_cnt += 1
            if diff_cnt == 1:
                queue.append([word, cnt + 1])
                answer = cnt + 1
                visited[i] = True        
    
    return answer if success else 0