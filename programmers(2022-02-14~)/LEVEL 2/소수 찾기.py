from itertools import permutations

def solution(numbers):
    answer = []
    n_list = []
    num_len = len(numbers)
    
    for i in numbers:
        n_list.append(i)
    
    for i in range(1, num_len+1):
        for j in list(permutations(n_list, i)):
            if isprime(int("".join(j))):
                answer.append(int("".join(j)))
    return len(set(answer))

def isprime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**(1/2)+1)):
            if n % i == 0:
                return False
        return True