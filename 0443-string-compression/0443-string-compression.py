class Solution:
    def compress(self, chars):
        i = 0
        result = 0

        while i < len(chars):
            j = i

            while j < len(chars) and chars[j] == chars[i]:
                j += 1

            chars[result] = chars[i]
            result += 1

            count = j - i

            if count > 1:
                for digit in str(count):
                    chars[result] = digit
                    result += 1

            i = j

        return result