# 문제 : n에 맞는 "IOI"패턴이 문자열안에서 몇번 나오는지 ?
# "IOI"를 어떻게 검사할건지 ?
# [i], [i+1], [i+2] = "IOI"인지 순차적으로 접근
# OOIOIOIOIIOII

# OOIOIOOOIIOII

# OOIOIOIOIIOII

# OOIOIOIOIOIOI 
pattern_value = int(input())
lens = int(input())
str = input()
result = 0
i = 0
pattern = 0
# while i < lens:
#   if str[i-1] == "I" and str[i] == "O" and str[i+1] == "I":
#     pattern += 1
#     if pattern == pattern_value:
#       result+=1
#       pattern -= 1
#     i+=2
#   else:
#     pattern = 0
#     i+=1
while i < lens-2:
  if str[i] == "I" and str[i+1] == "O" and str[i+2] == "I":
    pattern += 1
    if pattern == pattern_value:
      result+=1
      pattern -= 1
    i+=2
  else:
    pattern = 0
    i+=1

print(result)