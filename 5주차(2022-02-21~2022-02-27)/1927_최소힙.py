import heapq
import sys
input = sys.stdin.readline

n = int(input())
n_list = []

for _ in range(n):
  n_list.append(int(input()))

heap = []
for num in n_list:
  if num == 0 and len(heap) == 0:
    print(0)
  elif num ==0:
    print(heapq.heappop(heap))
  else:
    heapq.heappush(heap, num)