from bisect import bisect_left


def countSmaller(nums):
        arr, ans = sorted(nums), []
        for num in nums:
            i = bisect_left(arr,num)
            ans.append(i)
            del arr[i] 
        return ans 