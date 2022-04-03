def solution(s):
    stack = []
    
    for alpha in s:
        if len(stack) != 0 and stack[-1] == alpha:
            stack.pop()
        else:
            stack.append(alpha)
    
    if len(stack) == 0:
        return 1
    else:
        return 0
