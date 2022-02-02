# [1, 4, 10]
# [1, 3, 6]
# [1, 2, 3]
T = int(input())

for i in range(T):
  k = int(input())
  n = int(input())

  one_floor = [i for i in range(1,n+1)] # 0층 리스트 (리스트 컴프리헨션)
  # one_floor1 = []
  # for i in range(1,n+1):
  #   one_floor1.append(i)
  # print(one_floor, one_floor1)
  for _ in range(k): # k 층
    for i in range(1, n):
      one_floor[i] += one_floor[i-1]
      # one_floor[i] = one_floor[i] + one_floor[i-1]
  print(one_floor[-1])