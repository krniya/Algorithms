def findDifference(nums1, nums2):
    result = [[], []]
    nums1, nums2 = set(nums1), set(nums2)
    for n in nums1:
        if n not in nums2:
            result[0].append(n)
    for n in nums2:
        if n not in nums1:
            result[1].append(n)
    return result
