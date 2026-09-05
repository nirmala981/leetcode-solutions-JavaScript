import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        n = len(costs)

        left = []
        right = []

        i = 0
        j = n - 1

        # Fill left heap
        while i <= j and len(left) < candidates:
            heapq.heappush(left, costs[i])
            i += 1

        # Fill right heap
        while i <= j and len(right) < candidates:
            heapq.heappush(right, costs[j])
            j -= 1

        total = 0

        for _ in range(k):

            # Choose from left
            if not right or (left and left[0] <= right[0]):
                total += heapq.heappop(left)

                if i <= j:
                    heapq.heappush(left, costs[i])
                    i += 1

            # Choose from right
            else:
                total += heapq.heappop(right)

                if i <= j:
                    heapq.heappush(right, costs[j])
                    j -= 1

        return total