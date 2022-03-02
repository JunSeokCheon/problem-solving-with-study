# 유기농 배추
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph):
  que = deque()
  que.append((x,y))
  graph[y][x] = 0

  while que:
    row, column = que.popleft()
    for i in range(4):
      nx = row + dx[i]
      ny = column + dy[i]

      if nx < 0 or nx >= m or ny < 0 or ny >= n:
        continue
      if graph[ny][nx] == 1:
        que.append((nx,ny))
        graph[ny][nx] = 0

t = int(input())
for _ in range(t):
  result = 0
  m, n, k = map(int, input().split())
  t_list = [[0]*m for _ in range(n)]
  for _ in range(k):
    a, b = map(int, input().split())
    t_list[b][a] = 1

  for i in range(n):
    for j in range(m):
      if t_list[i][j] == 1:
        bfs(j, i, t_list)
        result += 1

  print(result)