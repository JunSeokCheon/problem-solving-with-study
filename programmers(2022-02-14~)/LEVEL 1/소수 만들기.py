def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**(1/2))+1):
            if num%i == 0:
                return False
        return True

def solution(nums):
    answer = 0
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                if is_prime(nums[i]+nums[j]+nums[k]):
                    answer += 1

    print(answer)

    return answer