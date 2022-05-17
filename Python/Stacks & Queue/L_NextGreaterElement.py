def nextGreaterElement(nums1, nums2):
        dic, stack = {}, []
        
        for num in nums2[::-1]:
            while stack and num > stack[-1]:
                stack.pop()
            if stack:
                dic[num] = stack[-1]
            stack.append(num)
            
        return [dic.get(num, -1) for num in nums1]

print(nextGreaterElement([4,1,2],[1,3,4,2]))