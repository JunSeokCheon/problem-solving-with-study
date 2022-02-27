import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
  num = int(input())

  if len(heap) == 0 and num == 0:
    print("0")
  elif num == 0:
    number, operation = heapq.heappop(heap)
    print(number*operation)
  else:
    if num >= 1:
      heapq.heappush(heap, [abs(num), 1])
    else:
      heapq.heappush(heap, [abs(num), -1])