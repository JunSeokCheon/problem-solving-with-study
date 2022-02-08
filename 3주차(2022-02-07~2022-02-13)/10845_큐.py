import sys
input = sys.stdin.readline
n = int(input())
que = []
for _ in range(n):
  temp = list(map(str, input().split()))
  
  if temp[0] == "push":
    que.append(temp[1])
  elif temp[0] == "pop":
    if len(que) == 0:
      print(-1)
    else:
      pop_num = que.pop(0)
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