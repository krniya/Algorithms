def jumpGame(nums):
    goal = len(nums) - 1
    for i in range(len(nums)-1,-1,-1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0

print(jumpGame([2,4,3,1,3,4]))