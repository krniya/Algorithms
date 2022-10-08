def threeSumClosest(nums, target: int) -> int:
        nums.sort()
        clos = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            l,r = i+1, len(nums)-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == target:
                    return sum
                if abs(sum - target) < abs(clos - target):
                    clos = sum
                if sum < target:
                    l+=1
                elif sum > target:
                    r-=1
        return clos