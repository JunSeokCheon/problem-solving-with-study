n = int(input())
count = 0
str_s = '666'
while(True):
  if '666' in str(str_s):
    count += 1
  if count == n:
    print(str_s)
    break
  str_s = int(str_s) + 1