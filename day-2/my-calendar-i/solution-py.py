from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def lower_bound(self, x: int) -> int:
        # find first index i such that calendar[i][0] <= start

        l, r = 0, len(self.calendar)
        while l < r:
            mid = (l + r) >> 1
            if self.calendar[mid][0] < x:
                l = mid + 1
            else:
                r = mid

        return l

    def book(self, start: int, end: int) -> bool:
        index = self.lower_bound(start)
        if (index > 0 and self.calendar[index-1][1] > start) or (index < len(self.calendar) and self.calendar[index][0] < end):
            return False

        self.calendar.add((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
