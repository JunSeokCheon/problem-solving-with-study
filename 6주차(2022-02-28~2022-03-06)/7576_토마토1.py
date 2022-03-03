# 토마토
from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, sys.stdin.readline().split())
mn_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

que = deque()
for i in range(n):
  for j in range(m):
    if mn_list[i][j] == 1:
      que.append((i,j,0))

while que:
  x, y, day = que.popleft()

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    nday = day + 1

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
      continue
    if mn_list[nx][ny] == 0:
      que.append((nx,ny,nday))
      mn_list[nx][ny] = 1

for i in range(n):
  for j in range(m):
    if mn_list[i][j] == 0:
      day = -1
      break

print(day)