from typing import List


def sumSubarrayMins(arr) -> int:
    arr = [0]+arr
    result = [0]*len(arr)
    stack = [0]
    for i in range(len(arr)):
        while arr[stack[-1]] > arr[i]:
            stack.pop() 
        j = stack[-1]
        result[i] = result[j] + (i-j)*arr[i]
        stack.append(i)
    return sum(result) % (10**9+7)
    
    
def sumSubarrayMins(arr: List[int]) -> int:
    n = len(arr)
    left = [-1] * n 
    right = [n] * n
    stack = []

    for i, value in enumerate(arr):
        while stack and arr[stack[-1]] >= value:  
            stack.pop()  
        if stack:
            left[i] = stack[-1]  
        stack.append(i) 

    stack = [] 

    
    for i in range(n - 1, -1, -1):  
        while stack and arr[stack[-1]] > arr[i]: 
            stack.pop()  
        if stack:
            right[i] = stack[-1]  
        stack.append(i) 

    mod = 10**9 + 7 

    result = sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr)) % mod
    
    return result 