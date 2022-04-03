# sorted ? : XWY, WXA -> X, W | W, X -> 똑같은 걸로 취급해야함 (정렬)
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for cour in course:
        result = []
        for order in orders:
            for combin in combinations(sorted(order), cour):
                result.append("".join(combin))

        counter_result = Counter(result).most_common()
        if len(counter_result) != 0:
            max = counter_result[0][1]
        
        for key, values in counter_result:
            if values > 1 and values >= max:
                answer.append(key)
    answer.sort()
    
    return answer