import numpy as np

def solution(arr1, arr2):
    answer = [[]]
    answer = np.dot(arr1, arr2).tolist()
    return answer