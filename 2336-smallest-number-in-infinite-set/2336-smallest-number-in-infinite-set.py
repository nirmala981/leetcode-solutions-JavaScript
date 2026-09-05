import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.heap = []
        self.seen = set()

    def popSmallest(self):
        if self.heap:
            num = heapq.heappop(self.heap)
            self.seen.remove(num)
            return num

        num = self.smallest
        self.smallest += 1
        return num

    def addBack(self, num):
        # Only add numbers that were already removed
        if num < self.smallest and num not in self.seen:
            heapq.heappush(self.heap, num)
            self.seen.add(num)