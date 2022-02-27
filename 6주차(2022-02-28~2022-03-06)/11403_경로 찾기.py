# a->k, k->b 가는 길이 있다면(1), a->b 도 가는길(1)이 존재한다.
n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
  for a in range(n):
    for b in range(n):
      if n_list[a][k] == 1 and n_list[k][b] == 1:
        n_list[a][b] = 1

for line in n_list:
  print(*line) # 리스트 앞에 *을 붙이면 [0 ,0 ,0 ,1 ,0 ,0 ,0] -> 0 0 0 1 0 0 0
# 콤마를 기준으로 나누고 싶다면 print(*line, sep=",") -> 0, 0, 0, 1, 0, 0, 0