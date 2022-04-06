def separate(p):
    open_count = 0
    close_count = 0
    
    for i in range(len(p)):
        if p[i] == "(":
            open_count += 1
        else:
            close_count += 1
        
        if open_count == close_count:
            return p[:i+1], p[i+1:]
        
def check(u):
    stack = []
    
    for i in u:
        if i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        return True
    else:
        return False

def solution(p):
    answer = ''
    
    if len(p) == 0:
        return ''
    
    u, v = separate(p)
 
    if check(u):
        return u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        
        for i in u[1:len(u)-1]:
            if i == "(":
                answer += ")"
            else:
                answer += "("
    
    
    return answer