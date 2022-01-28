# 2908 상수
n, m = map(str, input().split())
n_reverse = ''
m_reverse = ''
for i in range(2,-1,-1):
  n_reverse += n[i]
  m_reverse += m[i]

if int(m_reverse) > int(n_reverse):
  print(m_reverse)
else:
  print(n_reverse)