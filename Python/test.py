def minimumLines(sp) -> int:
        res,i = 0,1
        sp.sort()
        n = len(sp)
        if n<=1:
            return 0
        if n == 2:
            return 1
        def slope(x,y):
            return ((y[1]-x[1]) // (y[0]-x[0]))

        for i in range(1,n-1):
            if slope(sp[i],sp[i-1]) == slope(sp[i],sp[i+1]):
                continue
            res += 1
        return res + 1 

        
        


print(minimumLines([[72,98],[62,27],[32,7],[71,4],[25,19],[91,30],[52,73],[10,9],[99,71],
[47,22],[19,30],[80,63],[18,15],[48,17],[77,16],[46,27],[66,87],[55,84],[65,38],[30,9],[50,42],
[100,60],[75,73],[98,53],[22,80],[41,61],[37,47],[95,8],[51,81],[78,79],[57,95]]))
