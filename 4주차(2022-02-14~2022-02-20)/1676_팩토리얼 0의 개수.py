n = int(input())
count = 0

def fact(num):
  if num <= 1:
    return 1
  else:
    return num * fact(num-1)

result = str(fact(n))
for i in result[::-1]:
  if i == "0":
    count += 1
  else:
    break
print(count)