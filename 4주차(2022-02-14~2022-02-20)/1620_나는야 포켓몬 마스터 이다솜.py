# 시간초과 
# import sys

# n, m = map(int, sys.stdin.readline().rstrip().split())
# dic = {}
# n_list = []
# for i in range(1,n+1):
#   animal = sys.stdin.readline().rstrip()
#   dic[animal] = i

# for _ in range(m):
#   result = sys.stdin.readline().rstrip()
#   if result.isdigit():
#     for key, value in dic.items():
#       if value == result:
#         print(dic[int(key)])
#   else:
#     print(dic[result])  
# --------
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dic1 = {}
dic2 = {}
n_list = []
for i in range(1,n+1):
  animal = sys.stdin.readline().rstrip()
  dic1[animal] = i
  dic2[i] = animal

for _ in range(m):
  result = sys.stdin.readline().rstrip()
  if result.isdigit():
    print(dic2[int(result)])
  else:
    print(dic1[result])    