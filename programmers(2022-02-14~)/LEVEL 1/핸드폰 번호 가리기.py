def solution(phone_number):
    answer = ''
    m_len = len(phone_number)
    for i in phone_number[:m_len-4]:
        answer += "*"
    answer += phone_number[m_len-4:m_len]
    return answer