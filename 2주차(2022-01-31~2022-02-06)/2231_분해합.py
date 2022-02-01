# 분해합(주어진 것) = 생성자(구해야 하는것) + 생성자의 각 자리수의 합
# 시간복잡도/공간복잡도 -> 입력 형태 or 반복문 -> 개선해보자
n = int(input())
result = 0

for i in range(1,n+1):
  i_sum = 0
  for j in str(i):
    i_sum += int(j)
  
  result = i_sum + i
  
  if result == n:
    print(i)
    break

  if n == i:
    print(0)
    break

#  생성자(구해야 하는것) = 분해합(주어진 것) - 생성자의 각 자리수의 합
n = int(input())
result = 0
n_min = n - 9*len(str(n)) # 1-18까지는 음수가 나옴
if n_min > 1:
  n_min
else:
  n_min = 1

for i in range(n_min,n+1):
  i_sum = 0
  for j in str(i):
    i_sum += int(j)
  
  result = i_sum + i
  
  if result == n:
    print(i)
    break

  if n == i:
    print(0)
    break