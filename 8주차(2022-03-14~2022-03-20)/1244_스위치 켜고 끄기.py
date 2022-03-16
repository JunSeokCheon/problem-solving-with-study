import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int ,input().split()))
std_num = int(input())
for _ in range(std_num):
  gender, num = map(int, input().split())
  if gender == 1:
    for i in range(1,n+1):
      if i%num == 0:
        if n_list[i-1] == 0:
          n_list[i-1] = 1
        else:
          n_list[i-1] = 0
  else:
    i = 1
    if n_list[num-1] == 0:
      n_list[num-1] = 1
    else:
      n_list[num-1] = 0
    
    for _ in range(n//2):
      if (num-1-i) < 0 or (num-1+i) > n-1:
        break;
      if n_list[num-1-i] == n_list[num-1+i]:
        if n_list[num-1-i] == 0:
          n_list[num-1-i] = 1
        else:
          n_list[num-1-i] = 0

        if n_list[num-1+i] == 0:
          n_list[num-1+i] = 1
        else:
          n_list[num-1+i] = 0
      else:
        break
      i+=1

for i, value in enumerate(n_list):
  if i!=0 and i%20 == 0:
    print()
  print(value, end=" ")