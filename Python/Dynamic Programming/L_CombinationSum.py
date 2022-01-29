def combinationSum(candidates, target):
    def dfs(remain, combo, index):
        if remain == 0:
            result.append(combo)
            return
        for i in range(index, len(candy)):
            if candy[i] > remain:
                break
            dfs(remain - candy[i], combo + [candy[i]], i)
                
    candy = sorted(candidates)
    result = []
    dfs(target, [], 0)
    return result


print(combinationSum([2,3,4], 7))