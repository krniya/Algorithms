def merge(nums1, m: int, nums2, n: int) -> None:
        while n > 0:
            if m <= 0 or nums2[n-1] >= nums1[m-1]:  
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
        return nums1
print(merge([1,2,3,0,0,0], 3,[2,5,6], 3))