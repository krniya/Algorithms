# def countRectangles(rectangles, points):
#         res = [0] * len(points)
#         rectangles.sort()
#         for j, po in enumerate(points):
#             for i, rec in enumerate(rectangles):
#                 if po[0] <= rec[0] and po[1] <= rec[1]:
#                     res[j] = len(rectangles) - i
#                     break
#         return res

# print(countRectangles([[7,1],[2,6],[1,4],[5,2],[10,3],[2,4],[5,9]],
# [[10,3],[8,10],[2,3],[5,4],[8,5],[7,10],[6,6],[3,6]]))

from itertools import count
from turtle import circle


def countLatticePoints(circles):
        r = 201
        a = [[False]*r for _ in range(r)]
        def helper(X, Y, r):
            for x in range(X-r, X+r+1):
                for y in range(Y-r, Y+r+1):
                    if (X - x)**2+(Y - y)**2 <= r**2:
                        a[y][x] = True
        for temp in circles:
            x, y, r = temp
            helper(x, y, r)
        res = 0
        for temp in a:
            res += sum(temp)
        return res

print(countLatticePoints([[2,2,2],[3,4,1]]))