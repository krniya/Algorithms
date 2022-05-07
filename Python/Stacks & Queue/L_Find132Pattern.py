def find132pattern(nums) -> bool:
        stack = []
        curMin = nums[0]
        
        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n > stack[-1][1]:
                return True
            stack.append([n,curMin])
            curMin = min(curMin, n)
        return False

print(find132pattern([3,1,4,2]))