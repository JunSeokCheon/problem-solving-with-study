from collections import deque

n = int(input())
m = int(input())
n_list = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
  a, b = map(int, input().split())
  n_list[a].append(b)
  n_list[b].append(a)

def bfs(n):
  count = 0
  visited[n] = 1
  que = deque([n])
  while que:
    x = que.popleft()
    for i in n_list[x]:
      if visited[i] == 0:
        que.append(i)
        visited[i] = 1
        count += 1
  return count

result = bfs(1)
print(result)