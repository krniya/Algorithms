from collections import deque


def dailyTemperatures(temperatures):
        ans = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        return ans

def dailyTemperatures1(temperatures):
        stack, out = [], []
        for i in range(len(temperatures)-1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            stack.append((temperatures[i], i))
            if len(stack) == 1:
                out.append(0)
            else:
                out.append(stack[-2][1] - stack[-1][1])
            
        return out[::-1]

def dailyTemperatures3(temperatures):
        res = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _ , prevIdx = stack.pop()
                res[prevIdx] = idx - prevIdx
            stack.append([temp, idx])
        return res
    
def dailyTemperatures4(temperatures):    
    deq = deque()
    res = [0] * len(temperatures)

    for i in range(len(temperatures) - 1, -1, -1):
        if not deq:
            deq.appendleft(i)
            res[i] = 0
        else:
            while deq and temperatures[i] >= temperatures[deq[0]]:
                deq.popleft()

            if not deq:
                res[i] = 0
            else:
                res[i] = deq[0] - i

            deq.appendleft(i)

    return res

print(dailyTemperatures1([73,74,75,71,69,72,76,73]))