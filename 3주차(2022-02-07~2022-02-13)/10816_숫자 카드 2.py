n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_dic = {}

for i in n_list:
  if i not in n_dic:
    n_dic[i] = 1
  else:
    n_dic[i] += 1

for j in m_list:
  if j in n_dic.keys():
    print(n_dic[j], end=" ")
  else:
    print(0, end=" ")