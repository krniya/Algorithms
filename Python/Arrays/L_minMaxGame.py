def minMaxGame(nums) -> int:
        while len(nums) > 1:
            new_num = []
            for i in range(0,len(nums),2):
                a = nums[i]
                b = nums[i+1]
                p = i // 2
                if p%2 == 0:
                    new_num.append(min(a,b))
                else:
                    new_num.append(max(a,b))
            nums = new_num
        return nums[0]



def minMaxGame(nums) -> int: 
        while len(nums)!=1:
            #we take a newnums everytime of size n//2
            newnums = [-1]*(len(nums)//2)
            for i in range(0,len(nums)//2):
                if i%2==0:
                    newnums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    newnums[i] = max(nums[2 * i], nums[2 * i + 1])
            nums = newnums
        return nums[0]