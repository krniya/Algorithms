def maxDistance(nums1, nums2) -> int:
        i,j=0,0
        md = 0
        while i < len(nums1) and j < len(nums2):
            if i<=j and nums1[i] <= nums2[j]:
                md = max(md, j-i)
                j+=1
            else:
                if nums1[i] > nums2[j] and i == j:
                    j+=1
                else:
                    i+=1
        return md