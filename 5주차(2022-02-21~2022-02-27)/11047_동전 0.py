n, m = map(int, input().split())
n_list = []
count = 0
for _ in range(n):
  coin = int(input())
  if coin > m:
    pass
  else:
    n_list.append(coin)

for i in range(len(n_list)-1, -1, -1):
  if m == 0:
    break
  if m < n_list[i]:
    continue
  count += m // n_list[i]
  m = m - ((m // n_list[i]) * n_list[i])

print(count)