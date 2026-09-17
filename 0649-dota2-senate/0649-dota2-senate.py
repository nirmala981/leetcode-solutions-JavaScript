from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        n = len(senate)

        radiant = deque()
        dire = deque()

        # Store positions
        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:

            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                # Radiant acts first
                radiant.append(r + n)
            else:
                # Dire acts first
                dire.append(d + n)

        if radiant:
            return "Radiant"
        else:
            return "Dire"