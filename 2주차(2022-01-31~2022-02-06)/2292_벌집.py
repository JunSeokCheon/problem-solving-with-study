# 1 6(2-7) 12(8-19) 18(20-37) ....
n = int(input())
start = 1
count = 1 # 숫자 1인 구역 찾기
upper = 6

while(start<n):
  start += upper
  count += 1
  upper += 6
  
print(count)