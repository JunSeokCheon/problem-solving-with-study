# 단지번호 붙이기
from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(sys.stdin.readline())
n_list = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
result = []

def bfs(x, y):
  num = 1
  que = deque()
  que.append((x,y))
  n_list[x][y] = 0

  while que:
    x_x, y_y = que.popleft()
    for i in range(4):
      nx = x_x + dx[i]
      ny = y_y + dy[i]

      if 0 > nx or nx >= n or 0 > ny or ny >= n:
        continue

      if n_list[nx][ny] == 1:
        que.append((nx,ny))
        n_list[nx][ny] = 0
        num += 1

  return num

for i in range(n):
  for j in range(n):
    if n_list[i][j] == 1:
      result.append(bfs(i,j))

result.sort()
print(len(result))
for i in result:
  print(i)