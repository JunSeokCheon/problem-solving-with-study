n = int(input())
n_list = list(map(int, input().split()))
count = 0

def isprime(num):
  if num == 1:
    return False
  else:
    for i in range(2, int(num**(1/2))+1):
      if num%i==0:
        return False
    return True

for i in n_list:
  if isprime(i):
    count += 1

print(count)