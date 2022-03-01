# DFS는 재귀/BFS는 큐나 데크
from collections import deque
n, m, v = map(int, input().split())
n_list = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  n_list[a].append(b)
  n_list[b].append(a)
visited = [0] * (n+1)

for i in range(1,n+1):
  n_list[i].sort()

def dfs(v):
  visited[v] = 1
  print(v, end=" ")
  for i in n_list[v]:
    if visited[i] == 0:
      dfs(i)


def bfs(v):
  visited[v] = 1
  que = deque([v])
  while que:
    t = que.popleft()
    print(t, end=" ")
    for i in n_list[t]:
      if visited[i] == 0:
        que.append(i)
        visited[i] = 1
    
dfs(v)
print()
visited = [0] * (n+1)
bfs(v)