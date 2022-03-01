# 숨바꼭질
# 5 17

# que 5
# i (4, 6, 10)   -> 1초
# que 4 6 10
# visited [   1   1      1]

# i ((3,,8), (,7,12), (9,11,20)  -> 2초

# i (((2,,),(,16)),((,8,14),(,13,24)),((8,10,18),(10,12,22),(19,21,40))) -> 3초

# i                                            (17(정답),19,36)                 -> 4초
from collections import deque

n, k = map(int, input().split())
MAX = 100000
visited = [0] * (MAX+1)

def bfs(v):
  que = deque([v])
  while que:
    x = que.popleft()
    if x == k:
      print(visited[x])
      break

    for i in (x-1, x+1, x*2):
      if visited[i] == 0:
        que.append(i)
        visited[i] = visited[x] + 1
  
bfs(n)