from collections import deque
n, k = map(int, input().split())
n_list = [i for i in range(1,n+1)] # 1 2 3 4 5 6 7
result = []
que = deque(n_list)

while(len(que) > 0):
  que.rotate(-(k-1)) # 3 4 5 6 7 1 2
  pop_num = que.popleft() # 4 5 6 7 1 2 | pop_num : 3
  result.append(pop_num)

print("<", end="")
for i in result:
  if result[len(result)-1] == i:
    print(i, end="")
  else:
    print(i, end=", ")
print(">")