n = int(input())
for _ in range(n):
  n = input()
  score = 0
  n_sum = 0
  for i in n:
    if i == "O":
      score += 1
      n_sum += score
    else:
      score = 0
  print(n_sum)