import sys
n = int(input())
n_list = []
for _ in range(n):
  n_list.append(int(sys.stdin.readline()))

n_list.sort()

for i in n_list:
  print(i)