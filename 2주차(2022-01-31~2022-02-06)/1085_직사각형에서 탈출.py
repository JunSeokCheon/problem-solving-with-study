x, y, w, h = map(int, input().split())
print(min(w-x, h-y, y-0, x-0))