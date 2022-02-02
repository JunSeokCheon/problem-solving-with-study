n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_max = -1
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if n_list[i]+n_list[j]+n_list[k] <= m:
        n_max = max(n_max, n_list[i]+n_list[j]+n_list[k])
print(n_max)