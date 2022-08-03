class MyCalendar:
    
    def __init__(self):
        self.calendar = {'start': -1, 'end': -1, 'next': {'start': float('inf'), 'end': float('inf')}}
    def book(self, start: int, end: int) -> bool:
        curr = self.calendar
        while start >= curr['end']:
            last, curr = curr, curr['next']
        if curr['start'] < end:
            return False
        last['next'] = {'start': start, 'end': end, 'next': curr}
        return True