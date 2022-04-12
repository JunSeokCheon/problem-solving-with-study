def solution(n):
    answer = 0
    answer = fibon(n)
    return answer%1234567

def fibon(n):
    fibo = [0, 1]

    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    
    return fibo[-1]