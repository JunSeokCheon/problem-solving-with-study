while(True):
  a = list(map(int, input().split()))
  if a[0] == 0 and a[1] == 0 and a[2] == 0:
    break
  sorted_a = sorted(a)
  if sorted_a[0]**2 + sorted_a[1]**2 == sorted_a[2]**2:
    print("right")
  else:
    print("wrong")