import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
  n, m = map(int, input().split())
  important = list(map(int, input().split()))
  important_index = list(range(n))
  important_index[m] = "answer"

  order = 0
  while(True):
    if important[0] == max(important): # 맨 처음 중요도가 최고 중요도라면
      order += 1

      if important_index[0] == "answer":
        print(order)
        break
      else: # 가장 최고 중요도이지만 찾고자하는 인덱스가 아니라면 제거
        important.pop(0)
        important_index.pop(0)
    else: # 맨 처음 중요도가 최고 중요도가 아니라면 맨 뒤로 보내기
      important.append(important.pop(0))
      important_index.append(important_index.pop(0))