class StockSpanner:
    
    def __init__(self):
        self.stockspan = []
        

    def next(self, price: int) -> int:
        op = 1
        while self.stockspan and self.stockspan[-1][0] <= price:
            op += self.stockspan.pop()[1]
        self.stockspan.append([price,op])
        return op

stockSpanner = StockSpanner()
print(stockSpanner.next(100))
print(stockSpanner.next(80) )
print(stockSpanner.next(60) )
print(stockSpanner.next(70) )
print(stockSpanner.next(60) )
print(stockSpanner.next(75) )
print(stockSpanner.next(85) )