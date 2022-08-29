from collections import deque

def solution(queue1, queue2):
    que1, que2 = deque(queue1), deque(queue2)
    que1_sum = sum(que1)
    que2_sum = sum(que2)
    half_sum = (que1_sum + que2_sum) // 2
    cnt = 0
    
    while que1 and que2:
        if que1_sum == half_sum:
            return cnt
        elif que1_sum > half_sum:
            que1_sum -= que1.popleft()
        else:
            que1.append(que2.popleft())
            que1_sum += que1[-1]
        cnt += 1
    
    return -1