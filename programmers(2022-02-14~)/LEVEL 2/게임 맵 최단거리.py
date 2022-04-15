from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    answer = 0
    flag = False
    
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    que = deque()
    que.append((0,0,1))
    visited[0][0] = 1
    
    while que:
        x, y, dist = que.popleft()

        if x == (len(maps)-1) and y == (len(maps[0])-1):
            flag = True
            break
            
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            ndist = dist + 1
            
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and visited[nx][ny] == 0:
                if maps[nx][ny] == 1:
                    que.append((nx,ny,ndist))
                    visited[nx][ny] = 1
                    
    if flag:
        return dist
    else:
        return -1