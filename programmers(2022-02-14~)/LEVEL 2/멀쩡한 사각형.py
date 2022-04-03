# 가로 / 세로로 붙여보면 4개의 칸이 비게 되는데 그것은 가로+세로 - (빈칸의 개수)
# 빈칸의 개수를 생각하면 가로 세로의 최대공약수

import math

def solution(w,h):
    return w * h - (w + h - math.gcd(w,h))