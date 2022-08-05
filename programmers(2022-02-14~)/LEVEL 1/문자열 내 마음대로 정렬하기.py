def solution(strings, n):
    answer = []
    for string in strings:
        answer.append((string[n], string))
    return [i[1] for i in sorted(answer, key = lambda x: (x[0], x[1]))]