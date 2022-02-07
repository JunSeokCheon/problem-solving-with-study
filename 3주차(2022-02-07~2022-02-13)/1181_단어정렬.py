n = int(input())
n_list = []
for _ in range(n):
  n_list.append(input())

sorted_list = sorted(set(n_list), key = lambda x : (len(x), x))
for i in sorted_list:
    print(i)