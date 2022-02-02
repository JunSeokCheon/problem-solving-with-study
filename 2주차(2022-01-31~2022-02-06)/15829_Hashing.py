# 핵심은 a,b,c같은 알파벳을 어떻게 숫자로 일괄적으로 나타낼 것인가?(문제에 답이 있다)
n = int(input())
s = input()
s_sum = 0

for i in range(n):
  s_sum += (int(ord(s[i]))-96)*(31**i)
print(s_sum%1234567891)