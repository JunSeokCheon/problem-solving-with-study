import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dic = {}

for _ in range(n):
  site, password = map(str, sys.stdin.readline().rstrip().split())
  dic[site] = password

for _ in range(m):
  result = sys.stdin.readline().rstrip()
  print(dic[result])