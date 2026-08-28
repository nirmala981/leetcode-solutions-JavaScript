class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels = "aeiou"
        count = 0

        # First window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        maximum = count

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1

            if s[i - k] in vowels:
                count -= 1

            maximum = max(maximum, count)

        return maximum