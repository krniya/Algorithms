def summaryRanges(nums):
        if not nums:
            return []
        res = []
        prev = first = nums[0]
        for n in nums[1:]:
            if prev + 1 == n:
                prev += 1
                continue
            else:
                if first != prev:
                    res.append(str(first) + "->" + str(prev))
                else:
                    res.append(str(prev))
                prev = first = n
        if first != prev:
            res.append(str(first) + "->" + str(prev))
        else:
            res.append(str(prev))
        return res