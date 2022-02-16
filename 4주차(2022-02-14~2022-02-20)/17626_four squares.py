import sys
n = int(sys.stdin.readline())

def four_squares(num):  
  if int(num**0.5) == num**0.5: # 25
    return 1

  for i in range(1, int(num**0.5)+1):  # 40 = 6^2 + 2^2(1~6)
    if int((num - i**2)**0.5) == (num - i**2)**0.5:
      return 2

  for i in range(1, int(num**0.5)+1): # 41 = 6^2 + 2^2 + 1^1
    for j in range(1, int((num-i**2)**0.5)+1):
      if int((num - i**2 -j**2)**0.5) == (num - i**2 -j**2)**0.5:
        return 3
  return 4

print(four_squares(n))