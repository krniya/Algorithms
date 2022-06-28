from operator import indexOf


class TenderManagement:
    def __init__(self, data) -> None:
        self.attrMap = {
            "Lead Time":[0,1],
            "Tender Value":[0,2],
            "Project Duration":[0,3],
            "Vendor Rating":[1,4],
        }
        self.tendData = data

    def tenderAttribute(self,tenderAtt):
        attr , pos = self.attrMap[tenderAtt]
        val = [x[pos] for x in self.tendData]
        if attr:
            return self.tendData[val.index(max(val))]
        else:
            return self.tendData[val.index(min(val))]

    def printSen(self, tenderAtt):
        vendorName = self.tenderAttribute(tenderAtt)
        return "Mr Maharaj, you should award the tender to " + vendorName