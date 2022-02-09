import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_list = list(map(int, input().split()))
start = 1
end = max(n_list)

while(start<=end):
  n_len = 0
  mid = (start+end) // 2
  # for i in n_list:
  #   if (i-mid) > 0:
  #     n_len += (i-mid)
  # ----------------------------------
  # n_rest = [i-mid if (i-mid) > 0 else 0 for i in n_list]
  # n_len = sum(n_rest)
  # ----------------------------------
  n_len = sum(i-mid if (i-mid) > 0 else 0 for i in n_list)
  
  if n_len >= m: # 절단기로 짜른 나무의 길이의 합이 내가 목표하는 나무 길이 합보다 크다는 의미는 ? -> 절단기 설정 높이를 더 키워야 한다. -> 절단기 높이의 최대 값
    start = mid + 1
  else:
    end = mid - 1 
print(end)