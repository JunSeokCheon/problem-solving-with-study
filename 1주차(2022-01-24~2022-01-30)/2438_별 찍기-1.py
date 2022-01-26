# 1. method : 공백 생각 x
n = int(input())
for i in range(1,n+1):
  print("*"*i)


# 2. method : 공백 생각 o
n = int(input())
for i in range(1,n+1):
  print("*"*i + " "*(n-i))