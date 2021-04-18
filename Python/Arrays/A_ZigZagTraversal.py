# O(n) | O(n)
def ZigZagTraversal(arr):
    height = len(arr) - 1
    width = len(arr[0]) - 1
    result = []
    row, col = 0, 0
    goingDown = True
    while not isOutOfBound(row, col, height, width):
        result.append(arr[row][col])
        if goingDown:
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result

def isOutOfBound(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width

print(ZigZagTraversal([[1,3,4,10],
                       [2,5,9,11],
                       [6,8,12,15],
                       [7,13,14,16]]))