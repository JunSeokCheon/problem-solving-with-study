def solution(numbers):
    answer = ''
    
    if sum(numbers) == 0:
        return "0"
    
    max_len = len(str(max(numbers)))
    numbers = list(map(str, numbers))
    # print(max(numbers))
    numbers = sorted(numbers, key = lambda x : x*max_len, reverse=True)
    answer = "".join(numbers)
    return answer

# 시간 초과
# import itertools 
# from itertools import permutations

# def solution(numbers):
#     answer = ''
#     num_max = 0
#     for i in list(permutations(numbers, len(numbers))):
#         if num_max <= int("".join(map(str,i))):
#             num_max = int("".join(map(str,i)))
    
#     return str(num_max)