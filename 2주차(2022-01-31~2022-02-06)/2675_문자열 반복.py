# 1. method (print의 end 사용)
n = int(input())
for _ in range(n):
  m, k = map(str,input().split())
  for i in k:
    print(i*int(m), end="")
  print("")


# 2. method (임의의 text 문자열 더하기)
n = int(input())
for _ in range(n):
  m, k = map(str,input().split())
  text= ""
  for i in k:
    text += int(m) * i
  print(text)