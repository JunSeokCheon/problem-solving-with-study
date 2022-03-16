# 1
# 2
# 3 5

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
b, c = map(int, input().split())
count = 0

for candi in n_list:
  candi -= b
  count += 1
  if candi > 0:
    if candi%c == 0:
      count += int(candi/c)
    else:
      count += int(candi/c)+1
  else:
    continue

print(count)