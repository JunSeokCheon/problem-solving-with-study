import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
que = deque()
for _ in range(n):
  temp = list(map(str, input().split()))
  
  if temp[0] == "push_front":
    que.appendleft(temp[1])
  elif temp[0] == "push_back":
    que.append(temp[1])
  elif temp[0] == "pop_front":
    if len(que) == 0:
      print(-1)
    else:
      pop_num = que.popleft()
      print(pop_num)
  elif temp[0] == "pop_back":
    if len(que) == 0:
      print(-1)
    else:
      pop_num = que.pop()
      print(pop_num)
  elif temp[0] == "size":
    print(len(que))
  elif temp[0] == "empty":
    if len(que) == 0:
      print(1)
    else:
      print(0)
  elif temp[0] == "front":
    if len(que) == 0:
      print(-1)
    else:
      print(que[0])
  else:
    if len(que) == 0:
      print(-1)
    else:
      print(que[len(que)-1])