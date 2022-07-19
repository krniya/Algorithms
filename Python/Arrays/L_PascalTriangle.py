def generate(numRows: int):
        res = [[1]]
        for row in range(numRows - 1):
            tempArr = [0] + res[-1] + [0]
            newArr = []
            for i in range(len(res[-1]) + 1):
                newArr.append(tempArr[i] + tempArr[i+1])
            res.append(newArr)
        return res