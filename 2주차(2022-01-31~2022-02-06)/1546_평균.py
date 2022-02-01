n = int(input())
n_list = list(map(int, input().split()))
max_num = max(n_list)
new_list = []
for i in n_list:
  new_list.append(i/max_num*100)
print(sum(new_list)/n)