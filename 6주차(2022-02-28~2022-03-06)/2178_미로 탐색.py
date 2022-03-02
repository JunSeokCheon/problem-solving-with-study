# 미로 탐색 (visited를 써도 됨)
# 4 6
# 110110
# 110110
# 111111
# 111101
# 
# 220890
# 230780
# 345678
# 456709
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())  # 세로/가로
miro = [list(map(int,input())) for _ in range(n)]

def bfs(x,y):
  que = deque()
  que.append((x,y))
  miro[y][x] = 1

  while que:
    temp_x, temp_y = que.popleft()
    if temp_x == (m-1) and temp_y == (n-1):
      print(miro[temp_y][temp_x])
      return
      
    for i in range(4):
      nx = temp_x + dx[i]
      ny = temp_y + dy[i]

      if 0 > nx or nx >= m or ny < 0 or ny >= n:
        continue
      if miro[ny][nx] == 1:
        miro[ny][nx] = miro[temp_y][temp_x] + 1
        que.append((nx,ny))
      
bfs(0,0)