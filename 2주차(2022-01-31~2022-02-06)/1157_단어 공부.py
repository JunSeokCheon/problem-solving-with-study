# 1157 단어공부 <upper, set, count, index> or 딕셔너리 사용
a = input().upper()
dic = {}
count = 0

for i in a:
  if i not in dic:
    dic[i] = 1
  else:
    dic[i] += 1

for x,y in dic.items():
  if y == max(dic.values()):
    count+=1

sorted_dic = sorted(dic.items(), key=lambda x: -x[1])

if count > 1:
  print("?")
else:
  print(sorted_dic[0][0])