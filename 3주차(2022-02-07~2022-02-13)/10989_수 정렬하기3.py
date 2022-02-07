import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for i in range(n):
  m = int(sys.stdin.readline().rstrip())
  num_list[m] = num_list[m] + 1

for i in range(10001):
  if num_list[i] != 0:
    for j in range(num_list[i]):
      print(i)