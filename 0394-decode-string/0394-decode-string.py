class Solution(object):
    def decodeString(self, s):
        num_stack = []
        string_stack = []

        num = 0
        current = ""

        for ch in s:

            # If digit
            if ch.isdigit():
                num = num * 10 + int(ch)

            # Opening bracket
            elif ch == '[':
                num_stack.append(num)
                string_stack.append(current)

                num = 0
                current = ""

            # Closing bracket
            elif ch == ']':
                repeat = num_stack.pop()
                previous = string_stack.pop()

                current = previous + current * repeat

            # Normal character
            else:
                current += ch

        return current