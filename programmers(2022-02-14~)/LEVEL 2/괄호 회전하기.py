def isstring(s):
    dic = {"[" : "]", "(" : ")", "{" : "}"}
    stack = []
    
    for string in s:
        if string == "[" or string == "(" or string == "{":
            stack.append(string)
        else:
            if len(stack) == 0:
                stack.append(string)
                break
            else:
                if dic[stack[-1]] == string:
                    stack.pop()
                else:
                    break
    if len(stack) == 0:
        return True
    else:
        return False

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        tmp = list(s[i:] + s[:i])
        
        if isstring(tmp):
            answer += 1

    return answer