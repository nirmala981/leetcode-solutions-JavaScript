import heapq

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        pairs = list(zip(nums1, nums2))

        # Sort by nums2 in descending order
        pairs.sort(key=lambda x: x[1], reverse=True)

        heap = []
        total = 0
        answer = 0

        for num1, num2 in pairs:

            # Add nums1 value
            heapq.heappush(heap, num1)
            total += num1

            # Keep only k largest nums1 values
            if len(heap) > k:
                total -= heapq.heappop(heap)

            # If we have k elements, calculate score
            if len(heap) == k:
                answer = max(answer, total * num2)

        return answer
        