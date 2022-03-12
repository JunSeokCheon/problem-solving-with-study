def solution(n):
    answer = 0
    result = ""
    real = 0
    while n > 0:
        rest = n%3
        n = n//3
        result += str(rest)
    
    for i in range(len(result)):
        real += (int(result[i]) * (3**(len(result)-i-1)))
    answer = real
    return answer