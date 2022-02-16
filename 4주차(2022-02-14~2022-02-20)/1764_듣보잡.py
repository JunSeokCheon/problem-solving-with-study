import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dic = {}
nm_list = []
result = []
for _ in range(n+m):
  nm_list.append(sys.stdin.readline().rstrip())

for name in nm_list:
  if name not in dic:
    dic[name] = 1
  else:
    dic[name] += 1

for key, values in dic.items():
  if values == 2:
    result.append(key)

result.sort()
print(len(result))
for i in result:
  print(i)