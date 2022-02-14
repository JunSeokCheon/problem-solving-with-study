# 랜선의 !최대! 길이를 찾는 것. (랜선의 개수가 목표하는 n과 같은 랜선은 많지만 거기서 최대 길이를 찾는 것이므로 난이도가 더 높음)
# 4 11
# 802
# 743
# 457
# 539

# start 1       1	201	201	201	201	201	201	201	201    start <= end
# end 802     400	400	299	249	224	211	205	202	200    print(end)
# mid 401     200	300	250	225	212	206	203	201	200
# n_len 4      11	11down	11down  10	10	10	10	10	11
k, n = map(int, input().split())
n_list = []

for _ in range(k):
  n_list.append(int(input()))

n_list.sort() # 이진탐색을 위해서는 정렬 필수
start = 1
end = max(n_list)

while(start<=end):
  n_len = 0
  mid = (start+end) // 2
  for i in n_list:
    n_len += (i//mid)      

  if n_len >= n:  # 랜선의 길이가 더 길 필요가 있다 <여기서 = 의 의미 파악> 최대길이
    start = mid + 1 # 현재 mid를 기준으로 오른쪽 구간 탐색 
  else:  # 랜선의 길이가 더 짧을 필요가 있다 
    end = mid - 1 # 현재 mid를 기준으로 왼쪽 구간 탐색
print(end) # 왜 end를 출력할까 ? 최대길이