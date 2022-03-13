n = int(input()) # 사진틀
rec = int(input()) # 총 추천 수
rec_std = list(map(int, input().split())) # 추천받은 학생 번호

dic = {}

for i, std in enumerate(rec_std):
  if std not in dic:
    if n > len(dic):
      dic[std] = [1, i]
    else:
      remove_list = sorted(dic.items(), key = lambda x : (x[1][0], x[1][1]))
      remove_std = remove_list[0][0]
      del dic[remove_std]
      dic[std] = [1, i]
  else:
    dic[std][0] += 1

sorted_list = sorted(dic.items(), key = lambda x : (x[0]))

for i in sorted_list:
  print(i[0], end=" ")
  