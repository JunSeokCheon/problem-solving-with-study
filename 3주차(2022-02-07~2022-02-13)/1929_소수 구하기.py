import sys
input = sys.stdin.readline
m, n = map(int, input().split())
n_list = []

def isprime(num):
  if num == 1:
    return False
  else:
    for i in range(2,int(num**(1/2)+1)):
      if num%i==0:
        return False
    return True

for i in range(m,n+1):
  if isprime(i):
    n_list.append(i)

for i in n_list:
  print(i)