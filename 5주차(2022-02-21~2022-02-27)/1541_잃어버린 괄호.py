# 삽질 한거..(결국 실패: 이유 몰?루)
# cal = input()
# print(cal.split("-"))
# cal_split = cal.split("-")
# result = 0
# for i, str in enumerate(cal_split):
#   if "+" in str:
#     cal_split[i] = eval(str) # eval 은 식(문자열로 된 식, 단일 숫자도 식이다)을 실행하는 함수 | 예외 "0000009"은 되지 않는다. 왜냐하면 파이썬에서는 10진법에서는 숫자 맨 앞에 0을 쓸 수 없다.
#   else:
#     cal_split[i] = int(str)

# print(cal_split)
# result += cal_split[0]
# for i in range(1, len(cal_split)):
#   result -= cal_split[i]

# print(result)
######## 삽질 : 만약 -20+30+40-10+20-30 이 온다면 ?
# *핵심* 
# 1. -가 나올 때 다음에 -가 나오면 그대로 처리, +가 나오면 묶어준다.
# 2. +가 나올 때 다음에 +가 나오면 더해주고, -가 나오면 +나왔던 것들을 다 더해주고, 뒤에 숫자를 다 빼준다.

# ex1. 10 + 20 + 30 + 40
# ex2.1. 20+30+40-10+20-30 -> 20+30+40-(10+20)-30
# ex2.2. -20+30+40-10+20-30 -> -(20+30+40)-(10+20)-30
# ex3.1. 25-35+15-25-30+15-20+30+40 -> 25-(35+15)-(25-30+15)-(20+30+40)
# ex3.2. 25+35+15-25-15+25-30+40-30+50 -> 25+35+15-25-(15+25)-(30+40)-(30+50)
cal = input()
sum = 0
cal_split = cal.split("-")

for num in cal_split[0].split("+"):
  sum += int(num)

for num in cal_split[1:]:
  for num_split in num.split("+"):
    sum -= int(num_split)

print(sum)