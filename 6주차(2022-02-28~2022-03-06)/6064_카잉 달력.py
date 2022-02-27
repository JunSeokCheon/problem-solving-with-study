n = int(input())
for _ in range(n):
  flag = 1
  m, n, x, y = map(int, input().split())
  while(x <= m*n):
    if x%n == y%n:
      print(x)
      flag = 0
      break
    x+=m
  if flag:
    print("-1")