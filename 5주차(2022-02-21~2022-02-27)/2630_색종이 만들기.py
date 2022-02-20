import sys
n = int(sys.stdin.readline())
n_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
wc = 0
bc = 0

def paper(x,y,n):
  global wc, bc
  color = n_list[x][y]

  for i in range(x,x+n):
    for j in range(y,y+n):
      if n_list[i][j] != color:
        paper(x, y, n//2)
        paper(x+n//2, y, n//2)
        paper(x, y+n//2, n//2)
        paper(x+n//2, y+n//2, n//2)
        return
  
  if color == 0:
    wc+=1
    return
  else:
    bc+=1
    return

paper(0,0,n);
print(wc);
print(bc);