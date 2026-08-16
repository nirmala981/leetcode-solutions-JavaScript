class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        maximum=max(candies)
        res=[]
        for can in candies:
            if can+extraCandies>=maximum:
               
                res.append(True)
            else:
                res.append(False)
        return res
                
        