def diagonalSum(mat) -> int:
        n = len(mat)
        diagnolSum = 0
        i,jl,jr = 0,0,n-1 
        while i < n:
            diagnolSum += mat[i][jl]
            diagnolSum += mat[i][jr]
            i+=1
            jl+=1
            jr-=1
        return diagnolSum if n%2==0 else diagnolSum - mat[n//2][n//2]