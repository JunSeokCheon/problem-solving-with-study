def solution(msg):
    answer = []
    index = {chr(e + 64): e for e in range(1, 27)}
    i, num = 0, 27
    
    while i < len(msg):
        tmp = ''
        for j in range(i, len(msg)):
            tmp += msg[j]
            print(tmp)
            if not tmp in index:
                answer.append(index[tmp[:-1]])
                # print(tmp[:-1])
                # print(tmp, answer)
                i = j
                index[tmp] = num
                num += 1
                break
        else:
            answer.append(index[msg[i:]])
            break
    return answer
