# n!/(k!*(n-k)!)
n, k = map(int, input().split())

def fact(num):
  if num <= 1: # num 1이하인 경우는 1로 통일
    return 1
  else:
    return num*fact(num-1)

print(int(fact(n)/(fact(k)*fact(n-k))))