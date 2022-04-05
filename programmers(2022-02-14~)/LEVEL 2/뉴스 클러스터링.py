import re, copy

def solution(str1, str2):
    str1_list = []
    str2_list = []
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    for i in range(len(str1)-1):
        str1_data = re.sub("[^a-z]", "", str1[i]+str1[i+1])
        if len(str1_data) == 2:
            str1_list.append(str1_data)
    
    for i in range(len(str2)-1):
        str2_data = re.sub("[^a-z]", "", str2[i]+str2[i+1])
        if len(str2_data) == 2:
            str2_list.append(str2_data)
    
    str1_duplicate = str1_list.copy()
    union = str1_list.copy()
    intersection = []
    
    for i in str2_list:
        if i not in str1_duplicate:
            union.append(i)
        else:
            str1_duplicate.remove(i)
    
    for i in str2_list:
        if i in str1_list:
            intersection.append(i)
            str1_list.remove(i)
    
    # print(union)
    # print(intersection)
    
    union_len = len(union)
    intersection_len = len(intersection)
    
    if union_len == 0 and intersection_len == 0:
        return 65536
    elif intersection_len == 0:
        return 0
    else:
        return int(intersection_len/union_len*65536)