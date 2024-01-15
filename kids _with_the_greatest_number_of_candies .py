class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        result=[]
        i=0
        while i<len(candies):
            if candies[i]+extraCandies>=max(candies):
                result.append(True)
            else:
                result.append(False)
            i+=1
        return result

obj=Solution()
result=obj.kidsWithCandies([4,2,1,1,2],1)
print(type(result[0]))
