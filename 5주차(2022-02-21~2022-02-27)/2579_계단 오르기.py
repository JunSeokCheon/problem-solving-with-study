n = int(input())
n_list = []
dp = []

for _ in range(n):
  n_list.append(int(input()))

if n == 1:
  dp.append(n_list[0])
  print(dp[n-1])
  exit()

if n == 2:
  dp.append(n_list[0])
  dp.append(max(n_list[0]+n_list[1], n_list[1]))
  print(dp[n-1])
  exit()

dp.append(n_list[0])
dp.append(max(n_list[0]+n_list[1], n_list[1]))
dp.append(max(n_list[0]+n_list[2], n_list[1]+n_list[2]))
for i in range(3,n):
  dp.append(max(dp[i-3]+n_list[i-1]+n_list[i], dp[i-2]+n_list[i]))

print(dp[n-1])