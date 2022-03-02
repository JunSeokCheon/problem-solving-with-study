from collections import deque

n, m = map(int, input().split())
n_list = [[] for _ in range(n+1)]
result = []
for _ in range(m):
  a, b = map(int, input().split())
  n_list[a].append(b)
  n_list[b].append(a)
  
def dfs(v):
  visited = [0] * (n+1)
  cabin = [0] * (n+1)
  que = deque()
  que.append(v)
  visited[v] = 1

  while que:
    x = que.popleft()
    for i in n_list[x]:
      if visited[i] == 0:
        que.append(i)
        cabin[i] = cabin[x] + 1
        visited[i] = 1
  # print(cabin)
  return sum(cabin)

for i in range(1, n+1):
  result.append(dfs(i))

print(result.index(min(result)) + 1)