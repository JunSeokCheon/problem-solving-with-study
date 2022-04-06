from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(place):
    
    p_list = []
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                p_list.append((i,j))
    
    for p in p_list:
        que = deque()
        que.append((p[0], p[1]))
        visited = [[0] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        visited[p[0]][p[1]] = 1
        
        while que:
            x, y = que.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<5 and 0<=ny<5 and visited[nx][ny] == 0:
                    if place[nx][ny] == "O":
                        que.append((nx,ny))
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[x][y] + 1
                    
                    if place[nx][ny] == "P" and distance[x][y] <= 1:
                        return 0
    return 1
    

def solution(places):
    answer = []
    
    for place in places:
        answer.append(bfs(place))
    return answer