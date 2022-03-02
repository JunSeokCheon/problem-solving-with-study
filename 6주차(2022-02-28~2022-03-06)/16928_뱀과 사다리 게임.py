from collections import deque

n, m = map(int, input().split())
dic = {}

for _ in range(n+m):
  a, b = map(int, input().split())
  dic[a] = b

visited = [-1] * 101 # 방문 확인 용도와 주사위를 몇번 굴리는지 확인 용도

que = deque()
que.append(1)
visited[1] = 0
# print(visited)
# print(dic)

while que:
  x = que.popleft()
  for i in range(1,7):
    next = i + x
    # 100에 해당하는 주사위 굴리는 횟수를 저장해야 하니깐 100 초과되면 break
    if next > 100:
      break

    if next in dic:
      next = dic[next]

    if visited[next] == -1:
      visited[next] = visited[x] + 1
      que.append(next)
# print(visited)
print(visited[100])