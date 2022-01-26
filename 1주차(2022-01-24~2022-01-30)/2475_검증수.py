n_list = list(map(int, input().split()))
total = 0
for i in n_list:
  total+=(i*i);
print(total%10)