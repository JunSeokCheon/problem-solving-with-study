# def solution(scoville, K):
#     answer = 0
#     while min(scoville) < K:
#         scoville.sort()
#         try:
#             scoville.append(scoville.pop(0) + (scoville.pop(0) * 2))
#         except:
#             return -1
#         answer+=1
#     return answer

import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for food in scoville:
        heapq.heappush(heap, food)
    
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except:
            return -1
        answer+=1
    return answer