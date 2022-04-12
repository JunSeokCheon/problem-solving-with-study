import math

def solution(arr):
    while len(arr) != 1:
        arr.append(lcm(arr.pop(0), arr.pop(0)))
    
    return arr.pop()

def lcm(a,b):
    return (a * b) // math.gcd(a,b)