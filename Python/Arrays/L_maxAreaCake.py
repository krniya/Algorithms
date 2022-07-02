def maxArea(h: int, w: int, hc, vc) -> int:
        hc.sort()
        vc.sort()
        mod = 10**9 + 7
        ver = [vc[0], w - vc[-1]]
        hor = [hc[0], h - hc[-1]]
        for i in range(1,len(hc)):
            hor.append(hc[i]-hc[i-1])
        for i in range(1,len(vc)):
            ver.append(vc[i]-vc[i-1])
        return (max(hor) * max(ver))%mod