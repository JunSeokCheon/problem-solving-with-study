n = int(input())
for _ in range(n):
  arr = [0,1,1,1,2,2]
  m = int(input())
  if m > 5:
    for i in range(6,m+1):
      arr.append(arr[i-1]+arr[i-5])
  print(arr[m])