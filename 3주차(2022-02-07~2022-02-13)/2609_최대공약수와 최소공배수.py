def GCD(m, n):
  if n == 0:
    return m
  else:
    return GCD(n, m%n)

m, n = map(int, input().split())
gcd = GCD(m,n)
print(gcd)
print((m*n)//gcd)