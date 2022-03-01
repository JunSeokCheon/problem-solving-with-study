# 연결 요소의 개수
# 1 -> 
# visited [0, 1, 1 , 0 0 1 0]
# que 2 5

# 2 -> 
# visited [0, 1, 1 , 0 0 1 0]
# que 5

# 5 -> 
# visited [0, 1, 1 , 0 0 1 0]
# que 
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
n_list = [[] for _ in range(n+1)]
visited = [0] * (n+1)
result = 0

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  n_list[a].append(b)
  n_list[b].append(a)

def bfs(n):
  visited[n] = 1
  que = deque([n])
  while que:
    x = que.popleft()
    for i in n_list[x]:
      if visited[i] == 0:
        que.append(i)
        visited[i] = 1
        
for i in range(1,n+1):
  if visited[i] == 0:
    bfs(i)
    result += 1

print(result)