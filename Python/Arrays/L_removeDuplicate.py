def removeDuplicate(nums):
    i = 1
    count = 0
    num = nums[0]
    while i < len(nums):
        if nums[i] == num:
            nums.pop(i)
            count += 1
        else:
            num = nums[i]
            i += 1
    return count


print(removeDuplicate([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
