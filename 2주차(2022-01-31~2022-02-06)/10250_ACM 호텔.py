n = int(input())
for _ in range(n):
  h, w, n = map(int, input().split())
  if n%h==0:
    print(int(h*100+n/h))
  elif h>n:
    print(int(n*100+1))
  else:
    print(int(n%h*100+n/h+1))