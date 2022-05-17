def dailyTemperatures(temperatures):
        ans = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        return ans

print(dailyTemperatures([73,74,75,71,69,72,76,73]))