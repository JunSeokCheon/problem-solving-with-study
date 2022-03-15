def solution(x, n):
    answer = []
    x_sum = 0
    for i in range(n):
        x_sum += x
        answer.append(x_sum)
    return answer