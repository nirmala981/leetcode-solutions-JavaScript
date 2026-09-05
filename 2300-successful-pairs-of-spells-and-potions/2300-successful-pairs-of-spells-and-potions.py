from bisect import bisect_left

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        n = len(potions)

        result = []

        for spell in spells:
            required = (success + spell - 1) // spell

            index = bisect_left(potions, required)

            result.append(n - index)

        return result
        