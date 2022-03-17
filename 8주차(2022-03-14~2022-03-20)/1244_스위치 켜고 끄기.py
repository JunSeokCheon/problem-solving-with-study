def check(num):
  if n_list[num] == 0:
    n_list[num] = 1
  else:
    n_list[num] = 0

n = int(input())
n_list = list(map(int, input().split()))
switch = int(input())

for _ in range(switch):
  gender, num = map(int, input().split())
  if gender == 1:
    for i in range(num, n+1):
      if i%num == 0:
        check(i-1)
  else:
    i = 1
    check(num-1)
    for _ in range(50):
      if (num-1-i) < 0 or (num-1+i) > n-1:
        break
      if n_list[num-1-i] == n_list[num-1+i]:
        check(num-1-i)
        check(num-1+i)
      else:
        break
      i+=1

for i, value in enumerate(n_list):
  if i!=0 and i%20 == 0:
    print()
  print(value, end=" ")
