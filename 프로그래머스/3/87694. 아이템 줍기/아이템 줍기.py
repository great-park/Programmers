from collections import deque
dx, dy = [0,0,1,-1], [1,-1,0,0]

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    
    # 2배를 왜 곱해야 하는가?
    # 특정 점에서 (1) 이어지는 경로가 아님에도 불구하고 (2) 1칸 떨어진 위치에서 다른 쪽으로 연결된 경로가 있는 경우
    # -> 코드 내에서 지날 수 있는 경로로 인식하기 때문에 이동 단위인 1보다 크게 만들어서 반례를 방지
    answer = 0
    MAX = 102  # 두배로 늘리기 때문에 최대 102
    # 테투리 그리기
    field = [[5] * MAX for _ in range(MAX)]  # 5는 맨처음 땅
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:  # 내부일 때
                    field[i][j] = 0
                elif field[i][j] != 0:  # 테두리일 때 그리고 이미 내부가 아닐 때
                    field[i][j] = 1  # 테투리랑 내부랑 겹치면 그건 내부

    # 길 찾기 (최단거리는 BFS)
    queue = deque()
    queue.append([characterX * 2, characterY * 2])
    visited = [[0] * MAX for _ in range(MAX)]
    visited[characterX*2][characterY*2] = 1
    
    while queue:
        x,y = queue.popleft()
        if x == itemX *2 and y == itemY *2:
            answer = (visited[x][y] - 1) // 2
            break
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if visited[nx][ny] == 0 and field[nx][ny] == 1:
                queue.append([nx,ny])
                visited[nx][ny] = visited[x][y] + 1
                

    return answer