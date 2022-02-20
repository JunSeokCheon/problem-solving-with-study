n = int(input())
n_list = list(map(int, input().split()))
sum = 0
part_sum = 0
n_list.sort()

for i in n_list:
  part_sum += i
  sum += part_sum

print(sum)