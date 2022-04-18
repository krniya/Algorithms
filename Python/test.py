def digitSum(s,k):
        while len(s) > k:
            a = list(s)
            s=""
            i=0
            while i < len(a):
                k1 = k
                sum = 0
                while i < len(a) and k1>0:
                    sum += int(a[i])
                    i+=1
                    k1-=1
                z = s + str(sum)
                s=z
        return s

print(digitSum("1111122225",3))

# def minRound(tasks):
#         hm = {}
#         for task in tasks:
#             if task in hm:
#                 hm[task] += 1
#             else:
#                 hm[task] = 0
#         res = 0
#         for v in hm.values():
#             if v == 1:
#                 return -1
#             op = v // 3
#             if v%3:
#                 op+=1
#             res+=op
#         return res

# print(minRound([2,2,3,3,2,4,4,4,4,4]))