def floodFill(image, sr, sc, newColor):
        m = len(image)
        n = len(image[0])
        def ff(i,j, cc):
            image[i][j] = newColor
            for ni,nj in [(-1,0),(0,-1),(0,1),(1,0)]:
                if 0<=i+ni<m and 0<=j+nj<n and image[i+ni][j+nj] == cc:
                    ff(i+ni,j+nj, cc)
        ff(sr,sc,image[sr][sc])
        return image


print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))