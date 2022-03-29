def solution(n):
    answer = ''
    nums = [1,2,4]
    
    while n > 0:
        n -= 1
        answer += str(nums[n%3])
        n = n // 3
    return answer[::-1]