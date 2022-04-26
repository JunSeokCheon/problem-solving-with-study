def zinlaw(num, n):
    result = ''
    notation = '0123456789ABCDEF'
    
    if num == 0:
        return '0'
    while num > 0:
        result = notation[num % n] + result
        num = num // n
    
    return result

def solution(n, t, m, p):
    answer = ''
    temp_str = ''
    
    for i in range(t*m):
        temp_str += zinlaw(i, n)
    
    for i in range(t):
        answer += temp_str[p-1 + m*i]
    
    return answer