from audioop import reverse


def maximumUnits(boxTypes, truckSize) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        res = 0
        for noOfBox, unitPerBox in boxTypes:
            if noOfBox > truckSize:
                res += truckSize * unitPerBox
                return res
            truckSize -= noOfBox
            res += noOfBox * unitPerBox
        return res

print(maximumUnits([[1,3],[2,2],[3,1]],4))