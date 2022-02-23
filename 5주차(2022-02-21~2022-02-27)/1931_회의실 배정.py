# 핵심 : 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 
# 기본적으로 가장 빨리 시작하는 회의부터 시작을 하되 만약 시작시간이 같은 회의가 연달아 올 때 처리를 어떻게 ? 
# ex. (4,5) (4,4)으로 입력이 들어올 때, 시작시간으로 정렬 하면 시작시간이 같다면 들어온 순으로 정렬이 되어서 아래 예제에서 [(0, 2), (1, 4), (4, 5), (4, 4), (7, 3)] 출력이 된다.
# 그러면 (4,4)를 고려하지 않기 때문에 최대 값이 되기 위해서 시작시간으로 정렬 후 -> 끝 시간으로 정렬하면 [(0, 2), (1, 4), (4, 5), (4, 5), (7, 3)] 해결이 된다.
# 정렬된 리스트에 각 시간을 연결해주면 간단하다. (i+1번째 시작시간이 i번째 끝시간보다 크거나 같으면 연결이 된다는 의미 )
# 5
# 1 4
# 7 3
# 0 2
# 4 5
# 4 4
import sys
input = sys.stdin.readline
n = int(input())
n_list = []
for _ in range(n):
  a, b = map(int, input().split())
  n_list.append((a,b))

# sorted_list = sorted(n_list, key = lambda x : (x[0],x[1])) # 시작시간 정렬 -> 끝 시간 정렬
# print(sorted_list)
sorted_list = sorted(n_list, key = lambda x : x[0])
sorted_list = sorted(sorted_list, key = lambda x : x[1])
# print(sorted_list)

end_time = sorted_list[0][1]
count = 1
for i in range(1, n):
  if end_time <= sorted_list[i][0]:
    count+=1
    end_time = sorted_list[i][1]

print(count)