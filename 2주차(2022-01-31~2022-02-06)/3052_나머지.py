n_list = []
for _ in range(10):
  n_list.append(int(input())%42)
print(len(set(n_list)))