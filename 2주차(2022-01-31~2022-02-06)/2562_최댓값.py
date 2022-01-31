n_list = []
for i in range(9):
  n_list.append(int(input()))

n_max = max(n_list)
print(n_max)
print(n_list.index(n_max)+1)