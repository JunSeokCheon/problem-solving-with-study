# # 시간 초과
# origin_str = input()
# explode_str = input()

# while explode_str in origin_str:
#     origin_str = origin_str.replace(explode_str, '')

# if len(origin_str) == 0:
#     print("FRULA")
# else:
#     print(origin_str)

# 스택
origin_str = input()
explode_str = input()
stack = []

for char in origin_str:
	stack.append(char)
	if len(origin_str) >= len(explode_str):
		if ''.join(stack[-len(explode_str):]) == explode_str:
			for _ in range(len(explode_str)):
				stack.pop()

stack = ''.join(stack)
if stack:
	print(stack)
else:
	print('FRULA')
