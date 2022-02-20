import sys
n, m = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
sum_list = [0]
part_num = 0

for num in n_list:
  part_num += num
  sum_list.append(part_num)

for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  print(sum_list[b]-sum_list[a-1])