from functools import lru_cache

def numDecodings(s:str) -> int:
    if len(s) == 0 or s is None:
        return 0
    def dfs(string):
        if len(string)>0:
            if string[0] == '0':
                return 0
        if string == "" or len(string) == 1:
            return 1
        if int(string[0:2]) <= 26:
            first = dfs(string[1:])
            second = dfs(string[2:])
            return first+second
        else:
            return dfs(string[1:])

    result_sum = dfs(s)
    return result_sum

print(numDecodings("1121"))