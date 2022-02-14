def solution(id_list, report, k):
    users = {name:[] for i, name in enumerate(id_list)}
    ban_users = {name:0 for i, name in enumerate(id_list)}
    answer = [ 0 for _ in range(len(id_list))]
    
    for temp in set(report):
        user, ban_user = temp.split(" ")
        users[user].append(ban_user)
        ban_users[ban_user] += 1
    
    for key, values in users.items():
        for value in values:
            if ban_users[value] >= k:
                answer[id_list.index(key)] += 1
    
    return answer