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
  if j not in n_dic: # n_dic.keys()
    print("0")
  else:
    print("1")