import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
  temp = list(map(str, input().split()))
  
  if temp[0] == "push":
    stack.append(temp[1])
  elif temp[0] == "pop":
    if len(stack) == 0:
      print(-1)
    else:
      pop_num = stack.pop()
      print(pop_num)
  elif temp[0] == "size":
    print(len(stack))
  elif temp[0] == "empty":
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  else:
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])