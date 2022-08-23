def solution(a, b):
    answer = 0
    if a >= b:
        big_num = a
        small_num = b
    else:
        big_num = b
        small_num = a
    
    if big_num == small_num:
        return big_num
    else:
        return sum(range(small_num, big_num+1))