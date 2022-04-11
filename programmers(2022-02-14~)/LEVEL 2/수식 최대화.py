from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0
    oper_list = []
    stack = []
    
    for i in expression:
        if i in ["*", "+", "-"]:
            oper_list.append(i)
    
    oper_list = list(set(oper_list))
    oper_permut = list(permutations(oper_list, len(oper_list)))
    
    for oper in oper_permut:
        answer = max(answer, abs(result(oper, expression)))
    
    return answer

def result(oper, expression):
    que = deque()
    num = ''
    for exp in expression:
        if exp.isdigit():
            num += exp
        else:
            que.append(num)
            que.append(exp)
            num = ''
    que.append(num)
    
    # print(oper)
    # print(que)
    
    for op in oper:
        que2 = deque()
        while len(que) != 0:
            tmp = que.popleft()
            if op == tmp:
                if tmp == "+":
                    cal = int(que2.pop()) + int(que.popleft())
                    que2.append(cal)
                elif tmp == "-":
                    cal = int(que2.pop()) - int(que.popleft())
                    que2.append(cal)
                elif tmp == "*":
                    cal = int(que2.pop()) * int(que.popleft())
                    que2.append(cal)
            else:
                que2.append(tmp)
        que = que2
    
    return que.pop()
    