# 시간초과 : 개선 필요(탐색하는 범위를 줄여야 함!)
# n, r, c = map(int, input().split())
# result = 0

# def z(x,y,n):
#   global result
#   if x == r and y == c:
#     print(result)
#     return
#   if n == 1:
#     result += 1
#     return

#   z(x,y,n//2)
#   z(x,y+n//2,n//2)
#   z(x+n//2,y,n//2)
#   z(x+n//2,y+n//2,n//2)
    
# z(0,0,2**n)

n, r, c = map(int, input().split())
result = 0

def z(x,y,n):
  global result
  if r == x and c == y:
    print(result)
    return
  if n == 1:
    result += 1
    return
  if not (x <=  r <= x+n   and y  <=   c <= y+n):
    result += n**2
    return
  z(x,y,n//2)
  z(x,y+n//2,n//2)
  z(x+n//2,y,n//2)
  z(x+n//2,y+n//2,n//2)

z(0,0,2**n)