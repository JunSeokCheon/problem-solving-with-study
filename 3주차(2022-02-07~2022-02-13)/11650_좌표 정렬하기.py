n = int(input())
n_list = []

for _ in range(n):
  w, t = map(int, input().split())
  n_list.append((w,t))

result = sorted(n_list, key = lambda x : (x[0],x[1]))
for i in range(n):
  print(result[i][0], result[i][1])