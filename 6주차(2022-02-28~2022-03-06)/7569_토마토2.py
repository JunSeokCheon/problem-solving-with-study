# 토마토2
# pypy3
from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
mnh_list = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

que = deque()
for k in range(h):
  for i in range(n):
    for j in range(m):
      if mnh_list[k][i][j] == 1:
        que.append((k,i,j,0))

while que:
  x, y, z, day = que.popleft()

  for i in range(6):
    nx = x + dx[i]
    ny = y + dy[i]
    nz = z + dz[i]
    nday = day + 1

    if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
      continue
    if mnh_list[nx][ny][nz] == 0:
      que.append((nx,ny,nz,nday))
      mnh_list[nx][ny][nz] = 1

for k in range(h):
  for i in range(n):
    for j in range(m):
      if mnh_list[k][i][j] == 0:
        day = -1
        break

for i in range(h):
  for j in range(n):
    if mnh_list[i][j].count(0) > 0:
      day = -1
      break
print(day)