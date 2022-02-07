n = int(input())
n_list = []

for _ in range(n):
  w, t = map(int, input().split())
  n_list.append((w,t))

for i in range(n):
  count = 1
  for j in range(n):
    if i!=j:
      if (n_list[i][0] < n_list[j][0]) and (n_list[i][1] < n_list[j][1]):
        count += 1
  print(count, end=" ")