import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
  flag = 0
  m = int(sys.stdin.readline().rstrip())
  m_list = []
  for _ in range(m):
    m_list.append(sys.stdin.readline().rstrip())

  m_list.sort()
  for i in range(m-1):
    m_len = len(m_list[i])
    if m_list[i] == m_list[i+1][:m_len]:
      flag = 1
      break

  if flag == 1:
    print("NO")
  else:
    print("YES")