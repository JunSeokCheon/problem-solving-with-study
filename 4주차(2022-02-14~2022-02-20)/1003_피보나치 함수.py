# 0 - 1 0
# # 1 - 0 1


# # 2 - 1 1
# # 3 - 1 2
# # 4 - 2 3
# # 5 - 3 5
# # 6 - 5 8
# # 7 - 8 13
n = int(input())

for _ in range(n):
  zero_count = [1, 0]
  one_count = [0, 1]

  m = int(input())
  # zero_count[2] = one_count[1]
  # one_count[2] = zero_count[1] + one_count[1]

  if m > 1:
    for i in range(2,m+1):
      zero_count.append(one_count[i-1])
      one_count.append(zero_count[i-1]+one_count[i-1])
    
  print(zero_count[m], one_count[m])