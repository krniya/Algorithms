def findLength(nums1, nums2) -> int:
        strnum2 = ''.join([chr(x) for x in nums2])
        strmax = ''
        ans = 0
        for num in nums1:
            strmax += chr(num)
            if strmax in strnum2:
                ans = max(ans,len(strmax))
            else:
                strmax = strmax[1:]
        return ans