# 첫 시도 : permutation 이용(시간 초과)
# 두 번째 시도 : 문자열 기준 최대값 찾은 후 answer에 더해줘서 출력(3, 30 중 30이 더 큰 값으로 나옴)
# 마지막 시도 : 가장 긴 문자열 찾은 후 그 길이만큼 확장해줘서 정렬([0, 0, 0] -> "000" 이 나오기 때문에 예외처리)
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