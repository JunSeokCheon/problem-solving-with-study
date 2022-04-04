# 연구소
# 벽 세우기 + 3개의 벽 세우고 바이러스가 얼마나 퍼져는지 확인
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]

blank = 0
for i in range(n):
  for j in range(m):
    if n_list[i][j] == 0:
      blank += 1

real_result = 0

def bfs():
    visited = [[0] * m for _ in range(n)]
    global real_result

    virus = 0
    q = deque()
    for i in range(n):
        for j in range(m):
            if n_list[i][j] == 2:
                visited[i][j] = 1
                q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <=ny < m and visited[nx][ny]==0:
                if n_list[nx][ny] == 0:
                    visited[nx][ny] = 1
                    # graph[nx][ny] = 2
                    virus += 1
                    q.append((nx,ny))
            
    real_result = max(real_result,blank-virus)
  
def wall(cnt):
  if cnt == 3:
    bfs()
    return
  for i in range(n):
    for j in range(m):
      if n_list[i][j] == 0:
        n_list[i][j] = 1
        wall(cnt + 1)
        n_list[i][j] = 0

wall(0)
print(real_result - 3)