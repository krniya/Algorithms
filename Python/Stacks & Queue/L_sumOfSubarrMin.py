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