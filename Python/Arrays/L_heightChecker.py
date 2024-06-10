def heightChecker(heights) -> int:
    freq=[0]*101
    for x in heights:
        freq[x]+=1
    cnt=0
    for x in range(1, 101):
        f=freq[x]
        for i in range(cnt, cnt+f):
            heights[i]-=x
        cnt+=f
    return len(heights)-heights.count(0)