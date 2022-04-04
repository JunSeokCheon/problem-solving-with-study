def solution(s):
    s_min = 1001
    
    for opt in range(1, len(s) // 2 + 1):
        new_s = ''
        find = s[:opt]
        count = 1
        
        for j in range(opt, len(s), opt):
            if find == s[j:j+opt]:
                count += 1
            else:
                if count == 1:
                    count = ""
                new_s = new_s + str(count) + find
                find = s[j:j+opt]
                count = 1
        if count == 1:
            count = ""
        new_s = new_s + str(count) + find
    
        if s_min > len(new_s):
            s_min = len(new_s)
    
    if s_min > len(s):
        s_min = len(s) 
    
    return s_min