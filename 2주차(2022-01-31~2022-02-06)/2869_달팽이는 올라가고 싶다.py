# (a-b) -> 하루종안 올라간 거리, (v-b) -> 마지막 순간 낮에 정상에 오르는 경우 더이상 밤에 내려가지 않기 때문에 b를 빼준다.
# 두 가지경우 : 날짜(길이)가 딱 떨어지는 경우(ex. 3일, 5일), 날짜(길이)가 딱 떨어지지 않는 경우(ex. 3.2일, 5.7일 => 4일, 6일) (등산 비유)

# 2 1 5
# 1일차 2up 1down len:1
# 2일차 2up 1down len:2
# 3일차 2up 1down len:3
# 4일차 2up 1down(x) len:5(=goal)

# 3 1 6
# 1일차 3up 1down len:2
# 2일차 3up 1down len:4
# 3일차 3up 1down(x) len:7(>=goal(6)
a, b, v = map(int, input().split())

day = (v-b)%(a-b)
if day!=0:
  print((v-b)//(a-b)+1)
else:
  print((v-b)//(a-b))